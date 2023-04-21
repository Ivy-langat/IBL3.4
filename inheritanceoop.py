class Firstname:
    def __init__(self, name):
        if not name:
            raise ValueError("No name specified")
        self.name = name
#the class student takes in the name and course and returns a string stating the name is studying the course
class Student(Firstname):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def __str__ (self):
        return f"{self.name} is studying {self.course}"

class Teacher(Firstname):
    def __init__(self, name, units):
        super().__init__(name)
        self.units = units

    def __str__ (self):
        return f"{self.name} is teaching {self.units}"

def main():
    student = Student("Ivy", "Information science")
    teacher = Teacher("Chero", "Information science")
    print(student)
    print(teacher)

if __name__ =="__main__":
    main()