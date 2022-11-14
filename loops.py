user_sms = input('Enter any string: ')
upper_case = ''
vowels = ''
digit_counter = 0

for element in user_sms:
    if element.isdigit():
        digit_counter += 1
        if digit_counter == 3:
            print("The loop is interrupted")
            break
    else:
        if element.isupper():
            upper_case += element
        if element in "AaEeIiOoUuYy":
            vowels += element
        indexes_space = [index for index, x in enumerate(user_sms) if x in ' ']

print(upper_case)
print(indexes_space)
print(vowels)

