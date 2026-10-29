print(' *** File Error Handling ***')
filename, word = input('Enter file name and word : ').split()
try:
    filehandle = open(filename)
except FileNotFoundError:
    print(f'Error can not open file => {filename}')
else: 
    count = 0
    count1 = 0
    count2 = 0
    for line in filehandle:
        count += 1
        if word in line:
            count1 += 1
            count2 += count
    filehandle.close()
    print(f'Number of lines having "{word}" => {count1}')
    print(f'Sum of line number => {count2:,}')
    print(f'Total lines => {count:,}')
print('===== End of program =====')
    
