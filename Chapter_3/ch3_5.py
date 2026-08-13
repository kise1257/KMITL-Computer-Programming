print(" *** Transform second ***")
x = input("Enter seconds : ")

try:
    sec = int(x)

    if sec < 0:
        print("This number (" + x + ") is not VALID !!!")
    else:
        print(f"{sec:,} seconds ==> ", end="")

        w = sec // 604800
        sec = sec % 604800

        d = sec // 86400
        sec = sec % 86400

        h = sec // 3600
        sec = sec % 3600

        m = sec // 60
        sec = sec % 60

        if w > 0:
            print(w, "week" if w == 1 else "weeks", end=" ")
        if d > 0:
            print(d, "day" if d == 1 else "days", end=" ")
        if h > 0:
            print(h, "hour" if h == 1 else "hours", end=" ")
        if m > 0:
            print(m, "minute" if m == 1 else "minutes", end=" ")
        if sec > 0:
            print(sec, "second" if sec == 1 else "seconds", end="")

        print()

except:
    print("! ! ! please enter a whole number ==> " + x)
    print("This number (" + x + ") is not VALID !!!")

print("===== End of program =====")