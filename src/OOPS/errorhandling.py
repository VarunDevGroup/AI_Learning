from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    gender: int



emp=Employee("Varun Sharma",45,"male")

print(emp.name)