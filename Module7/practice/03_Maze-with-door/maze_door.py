# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def bfs(graph, start_vertex):
    start = start_vertex
    lengths = [None] * (len(graph))
    lengths[start] = 0
    queue = [start]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)

    return lengths


def dfs(graph, start_vertex):
    visited = [False] * (len(graph))

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)

    return visited



# Опишите список смежности по изображению лабиринта из файла task.md
graph_cloze = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8],  # 12
    [],  # 13
    [10],  # 14
    [],  # 15
]

graph_open = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [5, 8],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9, 11, 14],  # 10
    [10],  # 11
    [8, 13],  # 12
    [12],  # 13
    [10, 15],  # 14
    [14],  # 15
]

start_points = {5: 'S-1', 13: 'S-2', 3: 'S-3', 8: 'S-4'}

final = 0

key_list = (10, 7)

for vertex in start_points:
    visited = dfs(graph_cloze, vertex)
    if visited[final]:
        print(f"Из точки {start_points[vertex]} можно дойти до финиша, без ключа")
    elif visited[10] or visited[7]:
                visited = dfs(graph_open, vertex)
                if visited[final]:
                    print(f"Из точки {start_points[vertex]} можно дойти до финиша, с ключем")
                else:
                    print(f"Из точки {start_points[vertex]} нельзя  дойти до финиша")
    else:
        print(f"Из точки {start_points[vertex]} нельзя  дойти до финиша")



# Из точки S-... можно добраться до финиша, используя ключ
# ...
# Из точки S-... можно добраться до финиша без ключа
# ...
# Из точки S-... нельзя добраться до финиша
