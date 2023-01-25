from functools import reduce


liss =[1,2,3,4,5];

def func(num):
    return num>3;


fi = list(filter(func, liss));
print(fi)

################################################################# reduce######################################################




"""Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console."""
sc = reduce(lambda x , y : x+y , liss)
print(sc)