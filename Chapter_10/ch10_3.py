print(' *** Find number of lines for specific word ***')
filename, word = input('Enter file name and word : ').split()
filehandle = open(filename)
count = 0
count1 = 0
for line in filehandle:
    count += 1
    if word in line:
        count1 += 1
print(f'Number of lines having "{word}" => {count1}')
print(f'Total lines => {count}')
print()