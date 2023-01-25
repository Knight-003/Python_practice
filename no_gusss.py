n = 56
c = 5
temp = int()

while c != 0 :
    print("you have",c,"chances left")

    temp = int(input("enter a number"))
    if temp == n :
        print("you won")
        break
    elif temp > n:
        print("lower")
    elif temp < n :
        print("higher ")
    else :
        print("invalid input")
    
    c = c-1


