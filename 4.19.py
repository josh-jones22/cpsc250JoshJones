par = int(input())
score = int(input())
difference = score - par

if par < 3 or par > 6:
    print('Error')
elif difference == -2:
    print('Eagle')
elif difference == -1:
    print('Birdie')
elif difference == 0:
    print('Par')
elif difference == 1:
    print('Bogey')