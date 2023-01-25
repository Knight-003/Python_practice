class Students:
    leaves = 5



    @classmethod
    def change(cls, newentry):
        cls.leaves=newentry



nikhil = Students()
print(nikhil.leaves)


# if we want to access variable of class with instance then we have to use class methods




nikhil.change(6)
print(nikhil.leaves)
