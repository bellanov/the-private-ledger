# Python Naming Conventions

Overview of Python *naming conventions* when it comes to **public** and **private** variables, functions, etc.

| Type | Convention | Example |
|------|-----------|---------|
| Public variable/function | `snake_case` | `user_name`, `get_data()` |
| "Protected" (internal use) | `_single_underscore` | `_helper()`, `_cache` |
| "Private" (name-mangled) | `__double_underscore` | `__secret`, `__validate()` |
| Class | `PascalCase` | `UserAccount` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_RETRIES` |
| Module/package | `lowercase` | `utils`, `my_module` |

**Key notes:**
- Python has **no true private** — it's convention-based
- `__name` triggers **name mangling** (becomes `_ClassName__name`), making accidental access harder but not impossible
- `_name` signals "internal use" — respected by convention, not enforced
- Dunder methods (`__init__`, `__str__`) are special — don't invent your own

## Public Modifiers

By default, every attribute and method in a Python class is **public**. They can be freely *read*, *modified*, or *called* from inside the class, inside subclasses, or directly via an object instance outside the class.

```python
class Example:
    def __init__(self):
        self.data = "I am public"  # Public attribute

obj = Example()
print(obj.data)  # Accessible outside: Prints "I am public"
```

## Protected Modifiers (_)

To mark a member as protected, you prefix its name with a single **underscore** (e.g., _attribute).

- *The Reality:* The Python interpreter completely ignores this prefix. The variable remains fully functional and accessible from outside the class.
- *The Purpose:* It serves as a strong warning to other developers and static linters. It explicitly signals: "This is an internal implementation detail. Use it at your own risk, as it may change without notice."

```python
class Parent:
    def __init__(self):
        self._protected_data = "I am protected"

class Child(Parent):
    def display(self):
        print(self._protected_data)  # Intended usage: Allowed in subclass

obj = Child()
print(obj._protected_data)  # Technical reality: Still works outside, but discouraged!
```

## Private Modifiers

To mark a member as private, you prefix its name with a double underscore (e.g., `__attribute`). Note that names with double underscores at both the beginning and end (like `__init__`) are special **"dunder"** methods and are not *private*.

- *The Reality:* Python protects these fields through **Name Mangling**. The interpreter automatically rewrites the internal name by sticking the class name onto the front. It converts `__variable` into `_ClassName__variable`.

- *The Purpose:* If you try to call obj.__private_data from outside the class, Python will throw an AttributeError. This stops accidental overwrites or direct access, though you can still technically bypass it if you explicitly use the mangled name.