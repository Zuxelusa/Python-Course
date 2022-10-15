'''Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

def CheckTheFormula(X, Y, Z):
    if not (X or Y or Z) == (not X and not Y and not Z): 
        return True
    else: 
        return False

b = [True, False]
for i in range(len(b)):
    for j in range(len(b)):
        for k in range(len(b)):
            print(f"For X,Y,X values are '{b[i]}, {b[j]}, {b[k]}' accordingly the formula returns: {CheckTheFormula(b[i], b[j], b[k])}.")
