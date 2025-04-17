# Description: This file is used to read the layout of the grid from a file 
# and create a 2D array of the grid.
# 
def read_line(filename):
    lines = [line.strip() for line in open(filename, 'r')]
    print(lines)
    return lines

def create_map(lines):
    map = []
    w = len(lines[0])
    h = len(lines)
    print(w, h)
    for i in range(w):
        map.append([])
        for j in range(h):
            map[i].append(int(lines[j][i]))
    # print(map)
    return map

# if __name__ == '__main__':
#     lines = read_line('./enums/grid_test.txt')
#     map = create_map(lines)
#     print(map)
