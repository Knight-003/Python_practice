class Students:
    check1 = 1
    def __init__(self, aname, aage):
        self.name = aname              # it is a kind of encaptulation because the code for input and variable is encaptualated
        self.age = aage

    def func1(self):
        return (f"name {self.name}")

    @classmethod
    def creator(cls, string):
        temp = string.split("-")
        # print(*string.split("-"))
        return cls(*string.split("-"))

    @staticmethod
    def printe(string):
        print("good"+string)


class player():
    chek2 = 55 
    def __init__(self, aname, aage, agames):
        self.name = aname
        self.age = aage                         #we can create all operation in child class
        self.games = agames

    pass

class coolstudent(Students,player): # jis class ka name pahalae hoga uske according argument pass hoga agar method ya fir attribute ka name same ho
    def printee(self):
        print(self.games)
        print(super().chek2)

    pass


nikhil = coolstudent("nikhil", 18)
nikhil.games = "crik"

nikhil.printee()
print(nikhil.age)