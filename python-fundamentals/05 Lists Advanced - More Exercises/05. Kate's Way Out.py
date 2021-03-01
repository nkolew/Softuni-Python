def all_false(x):
    for check in x:
        if check:
            return False
    return True


def char_replace(string, x, y):
    temp = list(string[x])
    temp[y] = "#"
    temp = "".join(temp)
    maze[x] = temp


def kate(x):
    for row in x:
        if "k" in row:
            return x.index(row), row.index("k")


def way_out_path(x):
    way_out_map = []
    for a, row in enumerate(x):
        for b, column in enumerate(row):
            if column == " ":
                way_out_map.append([a, b])
    return way_out_map


def way_out(x, y, way_out_map):
    move = 0
    while True:
        found_a_way = [[x, y+1] in way_out_map, [x, y-1] in way_out_map,
                       [x+1, y] in way_out_map, [x-1, y] in way_out_map]
        found_a_way_value = [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]

        if x == maze_rows-1 or y == len(maze[0])-1 or y == 0:
            return f"Kate got out in {move+1} moves"

        if not all_false(found_a_way):
            x, y = found_a_way_value[found_a_way.index(True)]
            char_replace(maze, x, y)
            way_out_map.remove(found_a_way_value[found_a_way.index(True)])
            move += 1

        else:
            return "Kate cannot get out"


maze_rows = int(input())
maze = [input() for x in range(maze_rows)]
kate_row, kate_column = kate(maze)
map_to_freedom = way_out_path(maze)
print(way_out(kate_row, kate_column, map_to_freedom))
