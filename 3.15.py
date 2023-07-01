import math
phone_number = int(input())

end_num = phone_number % 10000
#print(end_num)
mid_num = (phone_number % 10000000 - end_num) / 10000
middle = math.ceil(mid_num)
#print(middle)
beg_num = phone_number // 10000000
#print(beg_num)
print(f"({beg_num}) {middle}-{end_num}")