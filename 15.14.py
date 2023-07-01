global recursions
global comparisons
recursions = 0
comparisons = 0


def binary_search(nums, target, lower, upper):
    # Declare global variables here.
    global recursions
    global comparisons

    # Increment the recursion count
    recursions += 1
    comparisons += 1

    # Choose an index midway between the lower and upper bounds
    index = (lower + upper) // 2

    # If target is found, return the index
    if target == nums[index]:
        comparisons += 1
        return index

    # If lower == upper, the target is not found
    if lower == upper:
        return -1

    # Call the function recursively on the appropriate half of the list
    if nums[index] < target:
        comparisons += 1
        return binary_search(nums, target, index + 1, upper)
    else:
        comparisons += 1
        return binary_search(nums, target, lower, index - 1)


if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]

    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons - 1}')