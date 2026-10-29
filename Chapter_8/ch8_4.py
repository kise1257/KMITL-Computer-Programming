
print(" *** Triangle Checker ***")
a, b, c = input("Enter side1 side2 side3 : ").split()

def triangleChecker(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    if a < 0 or b < 0 or c < 0:
        print("INPUTs cannot be negative.")
    elif a == 0 or b == 0 or c == 0:
        print("Side of triangle must not be zero.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("==> NOT VALID sides.")
    elif a == b and b == c:
        print("==> Equilateral Triangle.")
    elif a == b or a == c or b == c:
        print("==> Isosceles Triangle.")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("==> Right Triangle.")
    else:
        print("==> Triangle.")

triangleChecker(a, b, c)