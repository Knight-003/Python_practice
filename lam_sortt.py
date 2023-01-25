lis = [[3,18],[2,55],[1,44]]
def func(a):
    print(a[1])
    return a[1]

lis.sort(key=func)
print(lis)
# func(lis)
