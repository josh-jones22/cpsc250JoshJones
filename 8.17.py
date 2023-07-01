num_list = input().split()
neg_num = []
for num in num_list:
    if int(num) < 0:
        neg_num.append(int(num))
neg_num.sort()
neg_num.reverse()
output = ""
for num in neg_num:
    output += str(num) + " "

print(output, end='')