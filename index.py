'''class Employee:
    name = 'vasvxvbxanth'

class Student:
    name = 'siva'

class Details(Employee, Student):
    
    def details(self):
        print(self.name)

obj = Details()
 obj.details()

class Check:
    def identyfy(self):
        name = ["vasanth","siva"] 
        if name[1] == "siva" or type(name[1]) != tuple:
            print(True)
        else:
            print(False)
obj = Check()
obj.identyfy()'''
        

class Checking:
    def __init__(self):
        self.name = ["vasanth","siva"]
    def identyfy(self):
        if self.name[1] == "siva" and type(self.name[1]) != int:
            return True
        else:
            return False
obj = Checking()
print(obj.identyfy())

"dhsdflksflkdjf"






