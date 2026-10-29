print(" *** Recite the multiplication table ***")

def recite_same_day(arr1, arr2, arr3):
    for day in range(365):
        table1 = arr1[day % len(arr1)]
        table2 = arr2[day % len(arr2)]
        table3 = arr3[day % len(arr3)]

        if table1 == table2 and table2 == table3:
            return day + 1

    return -1


print("Enter pattern for child 1 to 3 (-1 for sep) : ", end="")

nums = list(map(int, input().split()))

patterns = []
current = []

for num in nums:
    if num == -1:
        patterns.append(current)
        current = []
    else:
        current.append(num)

child1 = patterns[0]
child2 = patterns[1]
child3 = patterns[2]

print()

print("Pattern for child 1 : ", end="")
print(*child1)

print("Pattern for child 2 : ", end="")
print(*child2)

print("Pattern for child 3 : ", end="")
print(*child3)

day = recite_same_day(child1, child2, child3)

if day == -1:
    print("This year they never recite same multiplication table !!!")
else:
    print("They recite same multiplication table in", day, "days")