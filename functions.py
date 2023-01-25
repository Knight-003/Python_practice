




def function1 ():
    """ this is doc string of function 1"""
    print("this is normal function " , 4+30)

def function2 (a,b) :

    print("this is function with arguments " , a+b)

def function3(a,b):

    return a+b



v = function3(5, 6)
function2(9, 10)
function1()
print(v)
print(function1.__doc__)

