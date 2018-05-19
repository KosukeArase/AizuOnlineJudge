"""
https://onlinejudge.u-aizu.ac.jp/#/courses/lesson/1/ALDS1/11/ALDS1_11_B
"""


class Node():
    def __init__(self, adjs=[], v=None):
        self.adjacents = adjs
        self.value = v
        self.visited = False
        self.found = 0
        self.finished = 0


class Graph():
    def __init__(self, nodes=[], head=None):
        self.head = None
        self.nodes = nodes


def dfs(graph, node, t):
    node.visited = True

    t += 1
    if not node.found:
        node.found = t

    for ind in node.adjacents:
        next_node = graph.nodes[ind]
        if not next_node.visited:
            t = dfs(graph, next_node, t)
    t += 1  
    node.finished = t
    return t


def main():
    n = int(input())
    graph = Graph(nodes=[None]*(n+1)) # THE 0th NODE IS DUMMY SINCE NODES ARE GIVEN WITH 1 ORIGIN

    for i in range(n):
        line = list(map(int, input().split()))
        node = Node(adjs=line[2:])
        graph.nodes[i+1] = node

    t = 0

    for node in graph.nodes[1:]: # because there may be multi graphs
        if not node.visited:
            graph.head = node
            t = dfs(graph, graph.head, t)

    for i, node in enumerate(graph.nodes[1:]):
        print(i+1, node.found, node.finished)


if __name__ == '__main__':
    main()
