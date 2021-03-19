import math

a = float(input(" The standart quadratic function is ax^2 + bx + c. Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

get = input("Press 1 to get characteristics of function: ")

def quadratic(a,b,c,x):
    try:
        return a * x ** + b * x + c
    except OverflowError:
        print("Sorry, the results are too large.")
        quit()

xS = (-b) / 2 * a
yS = quadratic(a,b,c,xS)

def yIntersect():
    return quadratic(a,b,c,0)

def xIntersect(a,b,c):
    p = b / a
    q = c/ a

    try:
        underSqrt = math.sqrt((p/2) **2 - q)

    except ValueError:
        return "no intersection"
              

    x1 = -(p/2) - underSqrt
    x2 = -(p/2) + underSqrt

    if x1 == x2:
        return( " x = " + str(x1))

    else:
        return( "x1 = " + str(x1), "x2 = " + str(x2))


def definition():
    return("definition: real numbers")

def yRange(a):
    if a < 0:
        return("range: y < " + str(yS))    
    else:
        return("range: y > " + str(yS))

def extreme(xS,yS,a,b):
    return("(" + str(xS) + "|" + str(yS) + ")")
    

if get == "1":
    print( " intersection with y-axis: " + str(yIntersect()) + "\n","intersection with x-axis: " + str(xIntersect(a,b,c)) + "\n",definition() + "\n",yRange(a) + "\n","extreme value: " + extreme(xS,yS,a,b))
