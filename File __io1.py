# "r" = read mode - default mode
# "w" = write mode
# "x" = create file if not exit
# "a" = add more content to file
# "t" = text mode - default mode
# "b" = binary mode
# "+" = read + write mode

f = open("souport.txt", "rt")
content = f.read(3)
# s = f.read(12222)
total = f.read()

print(content)
# print(s)
print(total)
f.close()