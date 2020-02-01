birthdays = {'Alice': 'April-1', 'Bappy': 'April-30', 'rafi': 'March-1'}
while True:
    name = input('Enter Your name to Find birthday, or (blank to quit)')
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have  birthday information for ', name)
        print('Do you want to add your birthdays? Type yes/no')
        agree = input()
        if agree =='no':
            continue
        elif agree == 'yes':
            bday = input('Enter Birthdays')
            birthdays[name] = bday
            print('Birthday database updated !')
            print(birthdays)