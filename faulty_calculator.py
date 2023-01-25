execp_set = (45,3,56,9,6)
print("please enter the operation ")
opr = input()
var1 = int(input()) # default input is always string
var2 = int(input())





if (opr == "*"): 
    if (var1 in execp_set and var2 in execp_set):
        print(var1+var2)
    else: print(var1 * var2)
        

        


if (opr == "/"):{

    print(var1 / var2)


}

if (opr == "+"):{

    print(var1 + var2)

}

if (opr == "-"):{

    print(var1 - var2)
}

