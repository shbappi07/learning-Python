while True:
    print('Enter Your Age: ')
    age = input()
    if age.isdecimal():
        break
    else:
        print('Age should be Number.')
        continue

while True:
    print('Enter Your Password. (Password should be letter and number)')
    password = input()
    if password.isalnum():
        break
    print('Password should be letter and number.')