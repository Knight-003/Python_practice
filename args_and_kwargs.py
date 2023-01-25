def function1(ara , *args):#args are used to pass list or tupple as tupple as a argument to a function .. we can chose any word 
                            #insted of args but all the normal argument should be before the arg  argument same applys for kwargs 
    print("i am normal {ara}")
    for x in args:
        print(x)

def function2(ara, **kwargs):
    print(f"i am 2nd normal {ara}")
    for key,value in kwargs.items():
        print(f"{key} has title {value}")


lsi = ["ram","mohan","sita"]

function1("output",*lsi)
dic = {"nikhil":"anand","mahindra":"dhoni"}
function2("output",**dic)