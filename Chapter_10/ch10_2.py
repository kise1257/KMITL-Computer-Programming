print(' *** Find Empty lines ***')
filename = input('Enter file name : ')
filehandle = open(filename)
count1 = 0
count2 = 0
for line in filehandle:
    count1 += 1
    if len(line.rstrip()) == 0:
        count2 += 1
print('Empty lines =>', count2)
print('Total lines =>', count1)
print()
