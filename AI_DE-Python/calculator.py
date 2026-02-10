# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     full_name = f_name + ' ' + l_name
#     return full_name

# print(format_name("ASwaNI", "jOGi"))
from calculator_logo import logo
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

val_addition = add
val_subtract = subtract
val_multiply = multiply
val_divide = divide


operations = {
    "+" : val_addition,
    "-" : val_subtract,
    "*" : val_multiply,
    "/" : val_divide,
    }
sequence_operation = 'N'
result = 0
def calculator():
    print(logo)
    first_num = float(input("First number ? : "))
    while 1==1:
        print(" + \n - \n * \n / \n")
        oper_to_perform = input(" what operation you want to perform from above ? : ")
        second_num = float(input("second number ? : "))


        compute = operations[oper_to_perform]
        result = compute(first_num, second_num)
        print(f"You have performed following {first_num} {oper_to_perform} {second_num} = {result}")
        sequence_operation = str(input("Do you want to continue with result or want to perform " \
                                    "new operation Y/N ? : ")).upper()
        if sequence_operation == 'Y':
            first_num = result 
        else:
            calculator()

calculator()






