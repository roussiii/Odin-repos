# students = ['Harry', 'Ron', 'Hermione', 'Draco', 'Neville', 'Ginny']
# houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# for student in students:
#     print(student)

# print("break")

# for i in range(len(students)):
#     print((i+1),"-", students[i])

# # Associate each student in students to a house in houses. Print the result.
# for i in range(len(students)):
#     print(students[i], "-", houses[i % len(houses)])


# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Griffindor",
#     "Ron": "Griffindor",
#     "Draco": "Slytherin",
#     "Neville": "Gryffindor",
#     "Ginny": "Gryffindor"
# }

# print(students)
# print(len(students))

# print(students["Hermione"])

# for student in students:
#     print(student, students[student], sep=", ")

students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "dog"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Draco", "house": "Slytherin", "patronus": "snake"},
    {"name": "Neville", "house": "Gryffindor", "patronus": "hare"},
    {"name": "Ginny", "house": "Gryffindor", "patronus": None},
]


for index, student in enumerate(students):
    print((index+1), student["name"], student["house"], student["patronus"], sep=", ")
