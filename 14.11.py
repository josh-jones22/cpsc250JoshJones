# TODO: Write recursive draw_triangle() function here.
def draw_triangle(base_length):
    if base_length>1:
        draw_triangle(base_length-2)
    print(" "*(9-base_length//2),end="")
    print("*"*base_length,end="")
    print()

if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)