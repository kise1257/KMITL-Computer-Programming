print(" *** Distance *** ")
u, a, t = input("Enter Velocity Acceleration Time: ").split(',')
u = float(u)
a = float(a)
t = float(t)
s = u *  t + 0.5 * a * t * t
print(f"Your Distance = {s:.2f}")