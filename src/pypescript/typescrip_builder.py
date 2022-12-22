from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: float

    def __post_init__(self):
        if type(self.name) is not str:
            raise TypeError("Field 'name' must be of type 'str'.")
        self.age = float(self.age)
        if self.age < 0:
            raise ValueError("Field 'age' cannot be negative.")



m = Person("haha", "asd")


print(m)