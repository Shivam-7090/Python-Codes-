
student = {
            "name": "Alice",
            "age": 21,
            "major": "Computer Science"
          }
print(student["name"]) 
student["grade"] = "A"
student["age"] = 22
del student["major"]
print(student)
for key, value in student.items():
    print(f"{key}: {value}")
