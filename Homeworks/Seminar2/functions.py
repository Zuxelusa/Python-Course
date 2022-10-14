def inputFloat(t = 0):# 0 - float, 1 - int
    while True:
        if t == 0: n = input("Input real number: ")
        if t == 1: n = input("Input integer number: ")
        try:
            if t == 0: return float(n)
            if t == 1: return int(n)
        except ValueError:
            print("Try again!")