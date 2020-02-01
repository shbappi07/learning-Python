import copy

# catNames = []
# while True:
#     print('enter Your cat name in position ' + str(len(catNames)) + ' On press enter to stop')
#     name = input()
#     if name == '':
#         break
#     else:
#         catNames = catNames + [name]
#
# for name in catNames:
#     print(''+name)
# =================
# supplies = ['pen', 'pencil', 'rubber', 'ereser', 'copy']
#
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' Supplies: ' + supplies[i])

# ================================
# myPets = ['ass', 'cow', 'goat', 'lamb']
# userPer = input('What is your pet name? ')
# if userPer in myPets:
#     print(userPer,' is your pet')
# else:
#     print('you do not have any pet in out list. ')

# =====================
# cat = ['fat', 'black', 'pretty']
# print(cat.index('black'))

# addCat = []
# while True:
#     userCatAdd = input('Enter Your Cat name or Type "s" to finish adding: ')
#     if userCatAdd != 'st':
#         addCat.append(userCatAdd)
#
#         continue
#     else:
#         break
# for i in range(len(addCat)):
#     #addCat.sort()
#     addCat.sort(reverse=True)
#     print(addCat[i])

# ====================================
spam = [1, 2, 3, 4, 5]
chese = copy.copy(spam)
chese[2] = 'salimul'
print('Print spams value ', spam)
print('Print cheses value ', chese)
