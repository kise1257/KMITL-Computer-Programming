print(" *** Finding circle area *** ")
diameter = input("Enter diameter : ")
diameter = float(diameter)
pi = 3.1415926
radius = diameter / 2
circleArea = pi * radius * radius
print("Circle area =", circleArea)
print(f"Circle area = {circleArea:0.02f}")     # Display the result to 2 decimal places.
print(f"whole number => {int(circleArea)}")   # Show only the integer part of the result.