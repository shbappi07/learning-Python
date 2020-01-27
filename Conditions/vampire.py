# name = input('Enter your name: ')
#
# if name == 'Alice':
# print('Hi, Alice.')
# elif age < 12:
# print('You are not Alice, kiddo.')
#  elif age > 100:
# print('You are not Alice, grannie.')
# elif age > 2000:
# print('Unlike you, Alice is not an undead, immortal vampire.')

while True:
    print('WHo are You? ')
    name = input()
    if name != 'joe':
        print('Authentication Failed')
        continue

    print('Hello Joe, What is the Password? ')
    password = input('Enter Your Password...')
    if password == 'sowrdfish':
        print('Access Granted. ')
        print('Welcome Joe, your password is, sowrdfish')
        print('Thanks')
        break
