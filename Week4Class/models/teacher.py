from .base import Person


class Teacher(Person):
    
    def __init__(self, name: str, age: int, email: str):
        self.age = age
        super().__init__(name, email)
    
    def addToClass(self, className: str):
        return f"I belong to {className}"