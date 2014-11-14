for i in range(15):
    if (i + 1) % 3 == 0 and not((i + 1) % 5 == 0):
        print("FIZZ")
    elif not((i + 1) % 3 == 0) and (i + 1) % 5 == 0:
        print("BUZZ")
    elif (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        print("FIZZBUZZ")
    else:
        print(i + 1)
