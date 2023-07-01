word = str(input())
spaceless_word = word.replace(" ", "")
new = spaceless_word[::-1]
if spaceless_word == new:
    print('palindrome: {}'.format(word))
else:
    print('not a palindrome: {}'.format(word))