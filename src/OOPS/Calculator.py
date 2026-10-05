class Calculator:

    appVersion="1.0.1"

    def __init__(self):
        self.appVersion="1.0.1"

    def add(self, a,b):
        return a+b

    def subtract(self,a,b):
        if (a>=b):
            return a-b
        else:
            return b-a

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        if b==0:
            return f"{self.appVersion}:  division by zero not possible"
        else:
            return a/b

    @classmethod
    def Describe(cls):
        return f"This is a calculator app with version {cls.appVersion}"

    @staticmethod
    def MoreAboutClass():
        return "This is a static method which is not dependent on class or object"
    
clc=Calculator()

print("Addition of 10 and 20 is: ", clc.add(10,20))
print("Subtraction of 10 and 20 is: ", clc.subtract(10,20))
print("Multiplication of 10 and 20 is: ", clc.multiply(10,20))
print("Division of 10 and 20 is: ", clc.divide(10,20))
print("INFO: ", clc.Describe())
print("More INFO: ", clc.MoreAboutClass())