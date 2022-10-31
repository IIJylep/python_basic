import ast
first_operand = ast.literal_eval(input(f"Enter the first operand: "))
second_operand = ast.literal_eval(input(f"Enter the second operand: "))
operation = str(input(f"Enter an operation: "))

print(f"Type first operand: {type(first_operand)}")
print(f"Type second operand: {type(second_operand)}")

if operation == '+':
    print(f'Result = {first_operand + second_operand}')

elif operation == '-':
    print(f'Result = {first_operand - second_operand}')

elif operation == '/' and second_operand == 0:
    print("You can't dividing on zero")

elif operation == '/':
    print(f'Result = {first_operand / second_operand}')

elif operation == '*':
    print(f'Result = {first_operand * second_operand}')

elif operation == '**':
    print(f'Result = {first_operand ** second_operand}')

else:
    print(f"Invalid operation between numbers ")
