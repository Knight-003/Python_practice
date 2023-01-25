# in python indexing of string always starts from 0
var1 = "heslow my name is nikhil"
var2 = "hellow my name is anand"
var3 = "HELLOW"
print(var1[0:5])   #the range taken as [0,5)
print(var1[0:]) 
print(var1[:19]) 
print(var1[0:78]) 
print(var1[0:10:3]) 

print(var1[::])
# negative index starts from -1
print(var1[-4 :])
print(var1[-4 :-1])

# some functions 
print(var1.isalnum())
print(var1.endswith("nikhil"))
print(var1.count("n"))
print(var2.capitalize())
print(var2.upper())
print(var3.lower())
print(var1.find("is"))
print(var1.replace("nikhil", "systems"))
print(var1[10:0:-1])


