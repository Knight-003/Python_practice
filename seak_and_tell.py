f = open("souport2.txt", "rt")
print(f.tell())#it tell wheather the file pointer is
print(f.readline())
print(f.tell())
f.seek(5)# the no. is letter no. of the string starting from 0
print(f.tell())
print(f.readline())
