catNames = []
while True:
    print('enter Your cat name in position ' + str(len(catNames)) + ' On press enter to stop')
    name = input()
    if name == '':
        break
    else:
        catNames = catNames + [name]

for name in catNames:
    print(''+name)
 