print(' *** Histogram ***')
filename, word = input('Enter file name and word : ').split()
try:
    filehandle = open(filename)
except FileNotFoundError:
    print(f'Error can not open file => {filename}')
else:
    count = 0
    count1 = 0
    wordoccurrences = 0
    charcount = {}
    for line in filehandle:
        count += 1
        occurrences = line.count(word)
        if occurrences > 0:
            wordoccurrences += occurrences
            count1 += count
            for char in line:
                if char.isalpha():
                    if char in charcount:
                        charcount[char] += 1
                    else:
                        charcount[char] = 1
    filehandle.close()
    print(f'Number of "{word}" => {wordoccurrences:,}')
    print(f'Sum of line number => {count1:,}')
    print(f'Total lines => {count:,}')
    def sort_key(item):
        return(item[1], item[0])
    topchar = sorted(charcount.items(), key=sort_key, reverse=True)[:3]
    maxcount = topchar[0][1]
    for char, num in topchar:
        stars = '*' * num
        print(f' {char}  => {stars:<{maxcount}} {num:02d}') 
print('===== End of program =====')
    