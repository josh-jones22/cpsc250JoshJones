user_input = input().split()
word = user_input[0]
number = user_input[1]

while (word != "quit"):
    print("Eating {0} {1} a day keeps you happy and healthy.".format(number, word))
    user_input = input().split()
    word = user_input[0]
    number = user_input[1]