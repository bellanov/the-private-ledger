from dataclasses import dataclass, field


@dataclass
class Query:
    table: str
    fields: list[str] = field(default_factory=list)
    conditions: list[str] = field(default_factory=list)
    limit: int | None = None

    def __repr__(self) -> str:
        fields = ", ".join(self.fields) or "*"
        where = f" WHERE {' AND '.join(self.conditions)}" if self.conditions else ""
        limit = f" LIMIT {self.limit}" if self.limit else ""
        return f"SELECT {fields} FROM {self.table}{where}{limit}"


class QueryBuilder:
    def __init__(self, table):
        self._table = table
        self._fields = []
        self._conditions = []
        self._limit = None

    def select(self, *fields):
        self._fields.extend(fields)
        return self  # enables chaining

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def limit(self, count):
        self._limit = count
        return self

    def build(self) -> Query:
        if not self._table:
            raise ValueError("Table name is required")
        return Query(self._table, self._fields, self._conditions, self._limit)


# --- Usage ---

query = (
    QueryBuilder("users")
    .select("id", "name", "email")
    .where("active = true")
    .where("age > 18")
    .limit(10)
    .build()
)

print(query)
# Output: SELECT id, name, email FROM users WHERE active = true AND age > 18 LIMIT 10
