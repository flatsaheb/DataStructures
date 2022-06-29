class ClassTest:
    def __init__(self,student_name):
        self.name = student_name
        self.marks = 500

    def fPrintGrade(self, *args):
        sum = 0
        for mark in args:
            sum = sum + mark
        print(sum)
        grade = (sum)/500*100
        print (grade)
        if grade < 30:
            return self.name + " has been Failed"
        elif grade >= 30 and grade <= 59.99:
            return self.name + " has obtained Second Division"
        elif grade >= 60 and grade <= 80:
            return self.name + " has obtained First Division"
        else:
            return self.name + " is extra-ordinary and obtained Distinction"

pstudent1 = ClassTest("Sunil")
print(pstudent1.fPrintGrade(100,30,100,20,50))
pstudent2 = ClassTest("Maria")
print (pstudent2.fPrintGrade(20,10,30,40,5))