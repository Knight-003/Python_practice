class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self, string):
        # self.var1 = "I am inside class B's constructor"
        # self.classvar1 = "Instance var in class B"          # in this the constructor is overide 
        super().__init__()    
        self.ck = string     
        # if we want to use methods and attributes of suber class then we use super .. in case of multiple inheritence super takes first parent class methode             
        # print(super().classvar1)


# a = A()
b = B("hello")
print(b.ck)

# print(b.special, b.var1, b.classvar1)