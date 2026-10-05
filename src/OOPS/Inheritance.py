#Inheritance 
#Single Inheritance
#Multilevel Inheritance
#Multiple Inheritance

class GrandFather:
    def __init__(self, name, birthplace):
        self.name=name
        self.birthplace=birthplace
        

    def Describe0(self):
        return f"THe avenger name is {self.name} with GrandFater of {self.birthplace} "


#Single Inheritance 
class Father(GrandFather):
    def __init__(self, name, birthplace, parentBirthPlace):
        super().__init__(name, birthplace)
        self.parentBirthPlace=parentBirthPlace

    def Describe1(self):
        return f"THe avenger name is {self.name} with GrandFater of {self.birthplace} and parent birthplace {self.parentBirthPlace}"

#multiple Inheritance
class Son(Father):
    def __init__(self, name, birthplace, parentBirthPlace, sonBirthPlace):
        super().__init__(name, birthplace,  parentBirthPlace)
        self.sonBirthPlace=sonBirthPlace

    def Describe(self):
        return f"THe avenger name is {self.name} with GrandFater of {self.birthplace} and parent birthplace {self.parentBirthPlace} and son birthplace {self.sonBirthPlace}"

boy=Son("John", "New York", "Los Angeles", "Chicago")

#print(boy.Describe0())
#print(boy.Describe1())
#print(boy.Describe())

class Father:
    def __init__(self, FatherName):
        self.FatherName = FatherName

    def DisplayFather(self):
        return f"The Father name is {self.FatherName}"  

class Mother:
    def __init__(self, MotherName):
        self.MotherName = MotherName

    def DisplayMother(self):
        return f"The Mother name is {self.MotherName}"  


class Child(Father, Mother):
    def __init__(self, FatherName, MotherName, ChildName):
        Father.__init__(self,FatherName)
        Mother.__init__(self,MotherName)
        self.ChildName = ChildName

    def DisplayChild(self):
        return f"The Child name is {self.ChildName}. He is son of {self.FatherName} and {self.MotherName}"


baby=Child("Krishna Kumar","Savitri", "Varun")
print(baby.DisplayFather())
print(baby.DisplayMother())
print(baby.DisplayChild())