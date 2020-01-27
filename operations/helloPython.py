print('Hello World')

print('What is your name? ')
yourName = input()
print('Welcome ', yourName)
nameLength = len(yourName)
print('Your name length is ', nameLength)
print('What is your age?')
# yourAge = int(input())
# print('You will be ', yourAge+5, 'after 5 years')

yourAge = input()
print('You will be ' + str(int(yourAge)+5) + ' after 5 years')

print('Thanks')
