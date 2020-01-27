#
# num1 = int(input('Enter a Number: '))
# userInput = input('What do you want to? "+, -, *, /" =')
#
# num2 = int(input('Enter another number: '))
#
# if userInput == '+':
#     print(num1,"+", num2, "=",num1+num2)
# elif userInput == '-':
#     print(num1,"-", num2, "=",num1-num2)
# elif userInput == '*':
#     print(num1, "*", num2, "=", num1 * num2)
# elif userInput == '/':
#     print(num1, "/", num2, "=", num1 / num2)
# else:
#
#     print('Please Select an Operator ')
#
# spam=0
# if spam ==10:
#     print('eggs')
#     if spam>5:
#         print('Becon')
#     else:
#         print('Ham')
#     print('Spam')
# print('spam')

value = int(input('Enter a number: '))
for number in range(value):
    print(number + 1, end='')
