def notMatched(varibl):
    while True:
        if varibl != 2:
            # print('Please Enter The Correct Number ')
            varibl = int(input('Please Enter The Correct Number: '))
        else:
            break


hiddenNumber = int(input('Take An Even number: '))
while True:
    if hiddenNumber%2 !=0:
        hiddenNumber = int(input('Please Take An Even number: '))
    else:
        break

times2 = int(input('Enter 2 to Times two: '))
notMatched(times2)

addSomtin = int(input('Add Presenter Number: '))

divide2 = int(input('Divide by two, Enter two: '))
notMatched(divide2)

subHidnNumber = int(input('Enter Your Taken Number: '))
while True:
    if subHidnNumber != hiddenNumber:
        subHidnNumber = int(input('Enter Your Taken Number: '))
    else:
        break

restNumber = (hiddenNumber * times2 + addSomtin) / 2 - subHidnNumber

print('The Rest number is: ', restNumber)
