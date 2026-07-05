from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 25

    def __post_init__(self):
        object.__setattr__(self, "sort_index", (self.age, self.name, self.job))

    def __str__(self) -> str:
        return f"name={self.name}, job={self.job}, age={self.age}, strength={self.strength}"


person1 = Person("Alice", "Engineer", 30, 80)
person2 = Person("Charlie", "Manager", 40)
person3 = Person("Charlie", "Manager", 40)

# Dataclasses are immutable, so we can't change the name after creation
# person1.name = "Bob"  # Error: cannot assign to field 'name'

print(person1)  # name=Alice, job=Engineer, age=30, strength=80
print(id(person2))  # <memory_address>
print(id(person3))  # <different_memory_address>

# Hmm, these are now equal!!!
print(person3 == person2)  # True

# Need to specify what this means
print(person1 < person2)  # Now we can compare them
