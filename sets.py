var1 = [1,2,3,4]
var2 = [3,4,5,6]
s = set(var1)
p= set(var2)
s.add(4) # in set only unique value is retained
s.add(5)
print(s)
u=s.union(p)
print(u)
i=s.intersection(p)
print(i)
s.remove(1)
print(s)
print(min(s))
print(min(var1))
