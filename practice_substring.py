s = input("please enter string")

output= str()
s_length = float(len(s))


for i in range(len(s)):

    if i ==0:
        output = output +s[i]
    
    elif s[i] != s[i-1]:
        if s[i] not in output:
            if float(i+1)<= float((s_length)/2):
                output = output +s[i]
            else:
                continue
    elif s[i] == s[i-1]:
        if float(i+1)< float((s_length)/2):
            output = s[i]
        else:
            continue
    

print(output)
print(len(output))
