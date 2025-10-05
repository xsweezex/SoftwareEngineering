from math import sqrt
def qwerty(a,b,c):
    x = float((a + b + c)) * 0.5
    return sqrt(x * (x-a) * (x-b) * (x-c))