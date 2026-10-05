class Avenger:
    def __init__(self, name, power,weapon="Gun"):
        self.name=name
        self.power=power
        self.weapon=weapon

    def Describe(self):
        return f"THe avenger name is {self.name} with power of {self.power} and weapon {self.weapon}"


ironMan=Avenger("Iron Man", "Intelligence")

print(ironMan.Describe())