'''Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.'''

def SegmentLength(x1, y1, x2, y2):
    import math
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

x1 = float(input("Input 1 dot X: "))
y1 = float(input("Input 1 dot Y: "))
x2 = float(input("Input 2 dot X: "))
y2 = float(input("Input 2 dot Y: "))

print(round(SegmentLength(x1, y1, x2, y2), 2))
