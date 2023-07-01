num = int(input())

max_number = None
numbers = []

for i in range(num):
    additional_num = float(input())

    if max_number is None or additional_num > max_number:
        max_number = additional_num

    numbers.append(additional_num)

for number in numbers:
    divided_number = number / max_number
    print(f'{divided_number:.2f}')