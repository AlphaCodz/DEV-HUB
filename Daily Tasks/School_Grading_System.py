
class SchoolGradingSystem:
    
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.grades = []
        self.percentage = 100.0
        
    def add_grade(self, grade_name):
        grade = float(input(f"{grade_name}:: "))
        self.grades.append({"gradeName ": grade_name, "grade": grade})
        
    def total(self):
        total = 0
        size = len(self.grades)
        if size == 0:
            return "There are no grades available"
        for subject in self.grades:
            total+=subject.grade
        return total // size * 100
    
    
#Actual Code

name = input("Student_Name:: ")
course = input("Student_course:: ")

Student1 = SchoolGradingSystem(name, course)

Student1.add_grade("English ")
Student1.add_grade("Math")

print(Student1.total())
        