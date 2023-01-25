import math
a = "arihant"
b = " arighat"

ssn = "it is nuclear submarine %s %s"%(a,b)
print(ssn)
ssbn = "it is nuclear submarine{}{}"
new = ssbn.format(a,b)
print(new)
# abobe methods are not so efficient

fast = f"ssbn is a balastic missile submarine ex... {a}"
print(fast)