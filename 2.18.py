nickels = int(input())
dimes = int(input())
quarters = int(input())
ntotal = nickels * 0.05
dtotal = dimes * 0.1
qtotal = quarters * 0.25
total = ntotal + dtotal+ qtotal
print(f'Amount: ${total:.2f}')