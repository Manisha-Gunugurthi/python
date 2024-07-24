
class student:
    def __init__(self,name,rollno,branch):
        self.name=name
        self.rollno=rollno
        self.branch=branch
    def display(self):
        print("Name is:",self.name)
        print("Roll no:",self.rollno)
        print("Branch :",self.branch)
obj=student("selena",101,"CSE")
obj.display()

