class Students:

    def __init__(self, aname, aage):
        self.name = aname
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


class programers(Students):
    def __init__(self, aname, aage, lang):
        self.name = aname
        self.age = aage                         #we can create all operation in child class
        self.languages = lang

    pass


# nikhil = Students()
vivek = Students("vivek", 20)
nikhil = programers.creator("nikhil-20-python")


print(nikhil.name, "\n", nikhil.languages)
nikhil.printe("hellow")
