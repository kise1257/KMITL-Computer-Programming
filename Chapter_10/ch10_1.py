print(' *** Find Total lines ***')
filename = input('Enter file name : ')
filehandle = open(filename)
print('property =>', filehandle)
count = 0
for line in filehandle:
    count += 1
filehandle.close()
print(f'Total lines : {count:,}')
print('===== End of progam =====')