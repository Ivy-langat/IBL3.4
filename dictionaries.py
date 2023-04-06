student = ["Kevin", "Sheldon", "Brian", "Johnte", "Joy"]
estates = ["Kasarani", "Exit 9", "Syokimau", "Kayole","Ngara"]

students = {
    "Kevin": "Kasarani",
    "Sheldon": "Exit 9",
    "Brian": "Syokimau",
    "Johnte": "Kayole",
    "Joy": "Ngara",
}

for student in student:
        print(student, students[student], sep= ",")
