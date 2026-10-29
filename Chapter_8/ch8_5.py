def generate_spiral(h, direction='right', word=None):
    h = int(h)
    matrix = [[None for j in range(h)] for i in range(h)]
    
    directions = {
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1),
        'up': (-1, 0)
    }
    
    dir_order = ['right', 'down', 'left', 'up']
    
    if direction not in directions:
        direction = 'right'
        
    if word is not None:
        word = str(word)
        values = []
        shift = 0
        repeat = 1
        while len(values) < h * h:
            for _ in range(repeat):
                for c in word:
                    values.append(chr(ord(c) + shift))
            shift += 1
            repeat += 1
        values = values[:h * h]
    else:
        values = list(range(1, h * h + 1))
        
    if h % 2 != 0:
        row = (h - 1) // 2
        col = (h - 1) // 2
    else:
        if direction == 'right':
            row, col = h // 2 - 1, h // 2 - 1
        elif direction == 'down':
            row, col = h // 2 - 1, h // 2
        elif direction == 'left':
            row, col = h // 2, h // 2
        elif direction == 'up':
            row, col = h // 2, h // 2 - 1
            
    current_direction = direction
    step = 1
    index = 0
    
    while index < h * h:
        for repeat in range(2):
            dr, dc = directions[current_direction]
            for count in range(step):
                if 0 <= row < h and 0 <= col < h and matrix[row][col] is None:
                    matrix[row][col] = values[index]
                    index += 1
                    if index == h * h: 
                        break
                row += dr
                col += dc
            if index == h * h: 
                break
            curr_idx = dir_order.index(current_direction)
            current_direction = dir_order[(curr_idx + 1) % 4]
        step += 1
        
    return matrix


def print_spiral(matrix):
    width = 0
    for row in matrix:
        for item in row:
            if len(str(item)) > width:
                width = len(str(item))
                
    for row in matrix:
        for item in row:
            print(str(item).rjust(width), end="  ")
        print()


print(" *** Center-starting Spiral Rectangle XXX ***")
inp = input("Enter side [direction] [word] : ")
args = inp.split()

spiral_rectangle = generate_spiral(*args)
print_spiral(spiral_rectangle)
print("===== End of program ======")