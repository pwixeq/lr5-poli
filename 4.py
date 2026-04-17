from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def dl(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])

        while queue:
            current_vertex = queue.popleft()

            if current_vertex not in visited:
                print(current_vertex, end=' ')
                visited.add(current_vertex)

                for neighbor in self.graph[current_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def gl(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            current_vertex = stack.pop()

            if current_vertex not in visited:
                print(current_vertex, end=' ')
                visited.add(current_vertex)

                for neighbor in reversed(self.graph[current_vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)


graph = Graph()

vert = ['A', 'B', 'C', 'D']
for vertex in vert:
    graph.add_vertex(vertex)

e = [('A', 'B'), ('A', 'C'), ('B', 'D')]
for edge in e:
    graph.add_edge(*edge)


print('Обход в ширину:')
graph.dl('A')

print('\nОбход в глубину:')
graph.gl('A')