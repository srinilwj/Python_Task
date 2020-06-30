user_input = input('Enter a string: ')
char_total = 0
digit_total = 0

for c in user_input:
    if c.isalpha():
        char_total += 1
    elif c.isdigit():
        digit_total += 1
print("Letters: ", char_total)
print("Digits: ", digit_total)