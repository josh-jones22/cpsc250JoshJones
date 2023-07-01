lst = [int(x) for x in input().split(" ")]
bounds = input().split(" ")
lower = int(bounds[0])
upper = int(bounds[1])
for i in lst:
    if(lower<=i and i<=upper):
        print(str(i),end=',')