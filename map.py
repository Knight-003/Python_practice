lss = ["1","2","3","4"]
pss = [1,2,3,4]

laa = list(map(int, lss))
print(laa)
sq = list(map(lambda x : x*x, pss))
print(sq)


def squ (x):
    return x*x


def cub (x):
    return x*x*x



func = [squ , cub]

for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))