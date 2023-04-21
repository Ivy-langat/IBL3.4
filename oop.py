class Student:
    def __init__(self, name, estate, course):
        if not name:
            raise ValueError("Please provide your name")
        if estate not in["Suna", "South B", "Karen"]:
            raise ValueError("Invalid Estate")
        self.name =name
        self.estate =estate
        self.course =course

    def __str__(self):
        return f"{self.name} is from {self.estate} and is doing {self.course}"

def main():
   # name =get_name()
    #estate = get_estate()
   # course = get_course()
    #print(f"{name} is from {estate} and is doing {course}")

    student= get_student()
    print(student)
def get_student():
    name = input("What is your name? ").strip()
    estate = input(" Which estate do you come from? ").strip()
    course = input(" Which course do you do? ").strip()
    return Student(name, estate, course)
    
#def get_name():
    #return input("What is your name? ").strip()

#def get_estate():
    #return input(" Which estate do you come from? ").strip()

#def get_course():
    #return input(" Which course do you do? ").strip()

if __name__ =="__main__":
    main()

