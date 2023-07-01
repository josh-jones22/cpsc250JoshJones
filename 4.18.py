
year = int(input())

if (year % 4) != 0:
    print(f'{year} - not a leap year')
elif (year % 100) != 0:
    print(f'{year} - leap year')
elif (year % 400) != 0:
    print(f'{year} - not a leap year')
else:
    print(f'{year} - leap year')