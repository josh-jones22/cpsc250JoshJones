def int_to_reverse_binary(integer_value):
    rev_string = ""
    while integer_value > 0:
        rev_string = rev_string + str(integer_value % 2)
        integer_value = integer_value // 2
    return rev_string

def string_reverse(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    integer_value = int(input())
    rev_string = int_to_reverse_binary(integer_value)
    binary_str = string_reverse(rev_string)
    print(binary_str)