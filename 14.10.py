# TODO: Write recursive digit_count() function here.
def digit_count(n):
    if n < 10:
        return 1
    else:
        return 1 + digit_count(n / 10)


if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)