counter = 0
elem = " "
row_numbers = 3
vowels = "AaEeIiOoUuYy"
while counter < 1:
    string = input('Enter any string: ')
    upper = (''.join(x for x in string if x.isupper()))
    print('Uppercase characters:', upper)
    print(f"Index of spaces: {[pos for pos, char in enumerate(string) if char == elem]}")
    final = [each for each in string if each in vowels]
    print(f"Vowel letters: {final}")
    bools = [c.isdigit() for c in string]
    c = 0
    for flag in bools:
        if flag:
            c +=1
        else:
            c = 0
        if c == row_numbers:
            print("3 digits in a row were entered. The loop is interrupted")
            counter += 1
            break
    else:
        print("The loop has been completed successfully")
        counter += 1

while True:
    first_data = str(input(f"Enter the first operand: "))
    second_data = str(input(f"Enter the second operand: "))
    operation = str(input(f"Enter an operation/Enter exit to complete: "))
    if operation == "exit":
        print("The process is completed")
        break
    if '.' in first_data:
        operand_one = float(first_data)
    else:
        operand_one = int(first_data)

    if '.' in second_data:
        operand_two = float(second_data)
    else:
        operand_two = int(second_data)

    if operation == '+':
        print(f'Result = {operand_one + operand_two}')

    elif operation == '-':
        print(f'Result = {operand_one - operand_two}')

    elif operation == '/' and operand_two == 0:
        print("You can't dividing on zero")

    elif operation == '/':
        print(f'Result = {operand_one / operand_two}')

    elif operation == '*':
        print(f'Result = {operand_one * operand_two}')

    elif operation == '**':
        print(f'Result = {operand_one ** operand_two}')
    else:
        print(f"Invalid operation between numbers ")
