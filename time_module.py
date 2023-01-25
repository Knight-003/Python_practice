import time
x=0
initial = time.time()
for x in range(100):
    print("this is time module")
print(f"the for loop time is {time.time()-initial}")
initial2 = time.time()
print(100*" this is time module\n")
print(f"the str time is {time.time()-initial2}")


loct = time.asctime(time.localtime(time.time()))
print(initial)

