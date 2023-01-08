from random import randint
from collections import deque


def show_mass(mass):
    for i in a:
        for j in i:
            print(j, end='\t')
        print()
    print()
    print()
    print()


def create_mass(col, row):
    return [[1 if randint(0, 100) < 20 else 0 for i in range(col)] for j in range(row)]


def check_merge(x, y):
    checker = lambda x, y: 0 <= x < rows and 0 <= y < columns and not a[x][y]
    ways = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    return [(x + i, y + j) for i, j in ways if checker(x + i, y + j)]


def create_graph(mass):
    graph = {}
    for x, line in enumerate(mass):
        for y, elem in enumerate(line):
            if not elem:
                graph[(x, y)] = check_merge(x, y)
    return graph


def wave_mass(mass, start_point):
    spisok = deque([start_point])
    visited = [start_point]
    count = 0
    while spisok:  # and not a[end_point[0]][end_point[1]]
        count += 1
        for _ in list(spisok):
            next_node = spisok.popleft()
            for elem in graf[next_node]:
                if elem not in visited:
                    mass[elem[0]][elem[-1]] = count
                    visited.append(elem)
                    spisok.append(elem)


def get_way(end_point, start_point):
    sequence = [end_point]
    while True:
        if sequence[-1] == start_point:
            break
        else:
            for i in graf[sequence[-1]]:
                if a[sequence[-1][0]][sequence[-1][-1]] - 1 == a[i[0]][i[-1]]:
                    sequence.append(i)
                    break
    return sequence


columns, rows = 25, 15
spoint = (8, 8)
epoint = (14, 24)

#a = create_mass(columns, rows)
a = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
     [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
     ]
show_mass(a)
graf = create_graph(a)
wave_mass(a, spoint)
seq = get_way(epoint, spoint)
show_mass(a)

print(f'{"->".join(repr(i) for i in seq[::-1])}')
