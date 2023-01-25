n = int(input("enter the no. of rows"))
b =int(input("enter 0 or 1"))
h = bool(b)



if h==True:


 for x in range(n):
   print(x * "*")



elif h==False:
 for x in range(n,0,-1):
   print(x * "*")