comparison_error: bool = 3 != 5

comparison_first_result: bool = 5 == 5
comparison_second_result: bool = 5 >= 5
comparison_third_result: bool = 5 <= 5

print(True or True or False)
print(True or True and False)
print(True and True or False)
print(True or True and (not False))
print((not True) or True or False)

print(bool(0) == bool(7))
print(bool( ) == bool(10-1))
print(bool(True) == bool(print("Text")))
print(bool(type(None)) == bool(id(None)))


