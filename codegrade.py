from datetime import date
current_date= date.today()
current_year= current_date.year

class CodeGradeUser:

    def __init__(self, username, institute):
        self.username= username
        self.institute= institute

    def hello(self):
        print(f"Hello {self.username} from {self.institute}")
    
class Student(CodeGradeUser):

    def __init__(self, username, institute, graduation_year):
        super().__init__(username, institute)
        self.graduation_year= graduation_year
    
    def graduated(self):
        return self.graduation_year<current_year
    
    def handin(self, assignment):
        if self.graduated():
            print (f"Sorry {self.username}")
        else:
            print(f"Thanks, {self.username}! Your submission {assignment} was successfully handed in!")
    
class Teacher(CodeGradeUser):

    def __init__(self, username, institute):
        super().__init__(username, institute)
    
    def teach(self):
        return ("Python is not just a snake, it is a fun coding language!")
    
    def grade(self, student, grade):
        if self.institute==student.institute:
            print(f"Teacher {self.username} graded {student.username} with grade {grade}.")
        else:
            print(f"You cannot grade {student.username} as they are from another institute.")
