# it is used to make a function attractive 
def dec1(func):
    def ret():
     print("execution started ...")
     func()
     print("executed ...")
    return ret


@dec1
def my_func():
    print("hellow world")

# my_func = dec1(my_func)

my_func()