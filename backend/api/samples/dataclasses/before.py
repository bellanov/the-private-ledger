class Person:
    name: str
    job: str
    age: int

    def __init__(self, name: str, job: str, age: int) -> None:
        self.name = name
        self.job = job
        self.age = age


person1 = Person("Alice", "Engineer", 30)
person2 = Person("Charlie", "Manager", 40)
person3 = Person("Charlie", "Manager", 40)

print(person1)  # <__main__.Person object at 0x...>
print(id(person2))  # <memory_address>
print(id(person3))  # <different_memory_address>

# Hmm, these should be equal!!!
print(person3 == person2)  # False

# Need to specify what this means
print(person1 < person2)
# TypeError: '<' not supported between instances of 'Person' and 'Person'
