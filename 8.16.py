input_str = input()
nums = [float(x) for x in input_str.split() if float(x) >= 0]
max_num = max(nums)
avg_num = sum(nums) / len(nums) if nums else 0
print(f"{max_num:.2f} {avg_num:.2f}")