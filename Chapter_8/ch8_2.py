
print("*** Sort avoid negative number ***")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sort_avoid_negative_num(arr):
    positive = []
    for num in arr:
        if num >= 0:
            positive.append(num)

    bubble_sort(positive)

    result = []
    index = 0

    for num in arr:
        if num < 0:
            result.append(num)
        else:
            result.append(positive[index])
            index += 1

    return result


inp = input("Enter Input : ")
arr = list(map(int, inp.split()))

print("Normal sort : ")
print(bubble_sort(arr.copy()))

print("sort avoid negative number : ")
print(sort_avoid_negative_num(arr))

print("===== End of program =====")
