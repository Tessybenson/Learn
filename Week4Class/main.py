from models.teacher import Teacher
from models.student import Students
from models.course import Course

def main():
    case = Teacher("tunji", 40, "tunjiman@yahoo.com")
    var = Students("kemi","kemi@gmail.com" )
    study = Course("Biology")
    print(var)
    print(case)
    print(study)
    print(case.addToClass("SS1"))


main()

