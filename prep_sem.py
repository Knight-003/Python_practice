# str = "hello i am nikhil"
# longest = max(str.split(), key=len)
# print(longest)
# print(len(longest))


#####################################################
# totContent = str()
# print("Enter the Name of File: ")
# fileName = str(input())
# fileHandle = open(fileName, "r")

# for content in fileHandle:
#     newContent = content.title()
#     totContent = totContent + newContent

# fileHandle.close()
# fileHandle = open(fileName, "w")
# fileHandle.write(totContent)

# print("All Words Capitalized Successfully!")
# fileHandle.close()
#######################################################
# lis1 = ["nikhil","is","great"]
# sr = " ".join(lis1)
# print(sr)
# print(type(sr))
###########################################################
# lis = [1,2,7,8]
# for i in lis:
#     if i == 7:
#         print("found")
#         break
############################################################
# Python program to display the Fibonacci sequence

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 10

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))
###################################################################
str = "hello i am nikhil "
ste = str[1:4:2]
print(ste)

    