class Students:

    def __init__(self, aname, aage):
        self.name = aname
        self.age = aage

    def func1(self):
        return (f"name {self.name}")

    @classmethod
    def creator(cls, string):
        temp = string.split("-")
        return cls(temp[0], temp[1])

    @staticmethod
    def good(string):
        print("you are good")
        return 89


# nikhil = Students()
vivek = Students("vivek", 20)
nikhil = Students.creator("nikhil-20")
print(nikhil.name)
# nikhil.name = "nikhil"


# print(nikhil.func1())
print(vivek.name)

b = vivek.good("bbb")

print(b)
print(nikhil.func1())
