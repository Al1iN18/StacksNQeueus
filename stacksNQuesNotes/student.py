class Student():
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        string ="Name:  "+ self.name + "\nGPA " + str(self.gpa)
        return string