student = {
    "name": "Ayo",
    "age": 2,
    "course": ["python", "javascript", "sql"],
    "grade": {
        "assignment": 2, 
        "test": 7,
        "exam": 25
    }
}

student.get("course")

print(student["course"].index("python"))

student["course"].append("html")

print(student.get("course"))

zodiac = ("libra", "gemini", "capricon")

Myself = "Teresa"

practise = dict.fromkeys(zodiac, Myself)

Mike = {}
print(Mike)
print(practise)
