'''Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

def CheckTheFormula(X, Y, Z):
    if not (X or Y or Z) == (not X and not Y and not Z): 
        return True
    else: 
        return False

print(f"For X,Y,X values are 'True, True, True' accordingly the formula returns: {CheckTheFormula(True, True, True)}.")
print(f"For X,Y,X values are 'True, True, False' accordingly the formula returns: {CheckTheFormula(True, True, False)}.")
print(f"For X,Y,X values are 'True, False, False' accordingly the formula returns: {CheckTheFormula(True, False, False)}.")
print(f"For X,Y,X values are 'False, False, False' accordingly the formula returns: {CheckTheFormula(False, False, False)}.")
print(f"For X,Y,X values are 'False, True, True' accordingly the formula returns: {CheckTheFormula(False, True, True)}.")
print(f"For X,Y,X values are 'False, False, True' accordingly the formula returns: {CheckTheFormula(False, False, True)}.")
print(f"For X,Y,X values are 'True, False, True' accordingly the formula returns: {CheckTheFormula(True, False, True)}.")
print(f"For X,Y,X values are 'False, True, False' accordingly the formula returns: {CheckTheFormula(False, True, False)}.")