def a ():
    print("hellow world")

b= a
del a
b()


def  ret(num):
    
    if num == 0:
        return print
    if num == 1 :
        return sum


a = ret(1)
print(a)


def execut(funcs):
    funcs("this")

execut(print)