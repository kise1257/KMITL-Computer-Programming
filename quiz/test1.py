b, h = (input("Enter Height Base : ")).split()
b = int(b)
h = int(h)
area = int((0.5*b*h))
print(f"Base: {b}, Height: {h}")
print(f"Area : {area}")


print("Calculate the sum of squares from 0 to N-1")
r, N = input('Enter r N : ').split()
r, N, total_str, total = int(r), int(N), '', 0
for i in range(N):
    num = r**i
    if total_str:
        total_str += '+'
    total_str += f"{num}"
    total += num
print(total_str,f' = {total}')

print(' Even largest and second largest')
even_list = [int(i) for i in input("Enter a list of numbers: ").split()
              if int(i) %2 == 0]
even_list.sort()
print(f" Even number: {even_list[-1]}")
print(f" Second largest even number: {even_list[-2]}")
if len(even_list) >= 2:
    print("There are not enough even numbers to find the second largest.")

print(" *** Fibonacci sequence ***")
a0, a1, n = input("Enter a0, a1, n: ").split()
a0, a1, n, fib_str, total = int(a0), int(a1), int(n), '', 0
for _ in range(n):
    a0, a1 = a1, a0 + a1
    total = a0 + a1
    fib_str += f"{a0} "
print(f"{fib_str} = {total}")

r, N = input('Enter r N : ').split()
r, N, total_str, total = int(r), int(N), '', 0
for i in range(N):
    num = r**i
    if total_str:
        total_str += '+'
        total_str += f'{num}'
        total += num
        print(f"{total_str} = {total}")