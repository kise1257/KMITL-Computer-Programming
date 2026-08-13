print(" *** Min Max Avg ***")
a, b, c = input("Enter 3 numbers : ").split()

a = float(a)
b = float(b)
c = float(c)

if a <= b and a <= c:
    mn = a
    if b <= c:
        mid = b
        mx = c
    else:
        mid = c
        mx = b
elif b <= a and b <= c:
    mn = b
    if a <= c:
        mid = a
        mx = c
    else:
        mid = c
        mx = a
else:
    mn = c
    if a <= b:
        mid = a
        mx = b
    else:
        mid = b
        mx = a

avg = (a + b + c) / 3

print("min, mid, max ==> %.1f, %.1f, %.1f" % (mn, mid, mx))
print("Average ==> %.2f" % avg)