import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain. '
    elif answerNumber == 2:
        return 'It is decideadly so'
    elif answerNumber == 3:
        return 'yes. '
    elif answerNumber == 4:
        return 'Ask again Later'
    elif answerNumber == 5:
        return 'Asl again Later'
    elif answerNumber == 6:
        return 'Concentrate and Ask.'
    elif answerNumber == 7:
        return 'My reply is NO. '
    elif answerNumber == 8:
        return 'Outlook not so good.'
    elif answerNumber == 9:
        return 'Very Doubtful'


# r = random.randint(1,9)

r = int(input('Select a random number between 1-9: '))

if r in range(1, 9):
    getAnswer(r)

fortune = getAnswer(r)
print(fortune)

