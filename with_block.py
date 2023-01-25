with open("souport.txt", "rt") as f:
    a= f.read() # in this we dont need to close file at end 
    print(a)


s = open("souport.txt")
e = s.read()
print(e)    # outside with open block all works fine 