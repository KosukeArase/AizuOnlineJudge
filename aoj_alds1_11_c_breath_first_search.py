"""
https://onlinejudge.u-aizu.ac.jp/#/courses/lesson/1/ALDS1/11/ALDS1_11_C
"""


class Node():
    def __init__(self, adjs=[], v=None):
        self.adjacents = adjs
        self.value = v
        self.visited = False
        self.distance = -1


class Graph():
    def __init__(self, nodes=[]): #, head=None):
        self.head = None
        self.nodes = nodes


def bfs(graph):
    queue = []
    queue.append(graph.head)
    graph.head.distance = 0
    graph.head.visited = True

    while len(queue) > 0:
        node = queue.pop(0)
        for idx in node.adjacents:
            child = graph.nodes[idx]
            if not child.visited:
                queue.append(child)
                child.distance = node.distance + 1
                child.visited = True


def main():
    n = int(input())
    graph = Graph(nodes=[None]*(n+1)) # THE 0th NODE IS DUMMY SINCE NODES ARE GIVEN WITH 1 ORIGIN

    for i in range(n):
        line = list(map(int, input().split()))
        node = Node(adjs=line[2:])
        graph.nodes[i+1] = node

    graph.head = graph.nodes[1]

    bfs(graph)

    for i, node in enumerate(graph.nodes[1:]):
        print(i+1, node.distance)


if __name__ == '__main__':
    main()
