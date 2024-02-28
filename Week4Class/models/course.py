class Course:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"The name of the course is {self.name}"
