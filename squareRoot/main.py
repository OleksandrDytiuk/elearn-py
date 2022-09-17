import math

#display message to user and request 3 integers from user. Return them as a b and c
def askValue(message):
    print(message)
    a = int(input('Enter a '))
    b = int(input('Enter b '))
    c = int(input('Enter c '))
    return a, b, c

#calculate discriminant and return its value
def discriminant(a, b, c):
    discr = b ** 2 - 4 * a * c
    print('D=', discr)
    return discr

#depending on the discriminant value (positive or zero) calculate and print roots.
#if discriminant is negative print that no real roots possible
def roots(discr, a, b, c):
    if discr == 0:
        x = (-1 * b) / (2 * a)
        print('One real root: ', x)
    elif discr > 0:
        x1 = (-1 * b + math.sqrt(discr)) / (2 * a)
        x2 = (-1 * b - math.sqrt(discr)) / (2 * a)
        print('Two real roots: ', x1, ' and ', x2)
    else:
        print('No real roots')

def solvSquare(a, b, c):
    discr = discriminant(a, b, c)
    roots(discr, a, b, c)

def main():
    message = 'Please enter values for square root equation ax^2+bx+c=0'
    a, b, c = askValue(message)
    solvSquare(a, b, c)
    print('Done')

main()