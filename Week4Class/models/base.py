from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def addToClass(self, className: str):
        return f"I belong to {className}"

    def __str__(self):
        return f"My name is {self.name} and my email adrress is {self.email}"

