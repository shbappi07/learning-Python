def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Can not divide by ero')


print(spam(12))
print(spam(0))
print(spam(1))
