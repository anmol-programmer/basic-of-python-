# Add methods to calculate total and grade in the Student class. 
class Student:
    marks = []
    def grade(self):
        name=input("Enter student name: ")
        self.marks.append((input("Enter marks of science, math,hindi,english ")).split())
        
        for item in self.marks:
            total= 0
            total=total+item
        print("Total marks of student", name, "is", total)
        if total >= 90:
            print("Grade: A")
        elif total >= 80:
            print("Grade: B")
        elif total >= 70:
            print("Grade: C")
        elif total >= 60:
            print("Grade: D")
        elif total >= 50:
            print("Grade: E")
        else:
            print("Grade: F")
        
s= Student()
s.grade()
    