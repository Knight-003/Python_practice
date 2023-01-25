dic1 = dict()
print(type(dic1))
key = str()
value = str()

for i in range(4):
    key = input("enter the key")
    value = input("enter the value ")
    dic1[key] = value

for its in dic1:
    print(its)
    