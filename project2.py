def get_number(number):
    while True:
        num = input("Enter number "+number+" : ")
        try:
            return float(num)
        except:
            print("Invalid Number! Try Again")


num1 = get_number('one')
num2 = get_number('two')

operator = input("Enter the operation sign : ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if(num2 == 0):
        print("Division by zero!!")
    else:
        print(num1/num2)
else:
    print("Invalid sign !!!")