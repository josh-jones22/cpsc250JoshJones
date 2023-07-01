a = input()
b = a[0]
c = a[2:]
if c.count(b) == 1:
    print(f"{c.count(b)} {b}")
if c.count(b) > 1:
    print(f"{c.count(b)} {b}'s")
if c.count(b) == 0:
    print(f"{c.count(b)} {b}'s")