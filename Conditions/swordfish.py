# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'sali':
#         break
# print('Access granted.')

while True:
    print('Enter Name: ')
    name=input()
    if name != 'salimul':
        continue
    print('Welcome, ',name)
    break
while True:
    passw = input('What is your Password: ')
    if passw !='sali':
        continue
    print('Please wait.......... ')
    break
if name == 'salimul' and passw == 'sali':
    print('Access grnted !')
else: print('User name and password did not matched. ')
