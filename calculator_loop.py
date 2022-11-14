while True:
    first_data = str(input(f"Enter the first operand: "))
    if first_data == "exit":
        print("The program has ended")
        break
    second_data = str(input(f"Enter the second operand: "))
    if second_data == "exit":
        print("The program has ended")
        break
    operation = str(input(f"Enter an operation: "))
    if operation == "exit":
        print("The program has ended")
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
