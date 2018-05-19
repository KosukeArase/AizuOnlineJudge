"""
https://onlinejudge.u-aizu.ac.jp/#/courses/lesson/1/ALDS1/8/ALDS1_8_C
"""


class TreeNode():
    def __init__(self, v=None, p=None, l=None, r=None):
        self.v = v
        self.p = p
        self.l = l
        self.r = r


class BinarySearchTree():
    def __init__(self, root=None):
        self.root = root

    def __insert(self, v, node):
        if node.v > v:
            if node.l:
                self.__insert(v, node.l)
            else:
                new_node = TreeNode(v=v, p=node)
                node.l = new_node
        elif node.v < v:
            if node.r:
                self.__insert(v, node.r)
            else:
                new_node = TreeNode(v=v, p=node)
                node.r = new_node
        else:
            raise ValueError

    def insert(self, v):
        if not self.root:
            node = TreeNode(v)
            self.root = node
        else:
            self.__insert(v, self.root)

    def __print_inorder(self, node):
        if node.l:
            self.__print_inorder(node.l) 
        print(' ' + str(node.v), end='')
        if node.r:
            self.__print_inorder(node.r)

    def __print_preorder(self, node):
        print(' ' + str(node.v), end='')
        if node.l:
            self.__print_preorder(node.l)
        if node.r:
            self.__print_preorder(node.r)
 
    def print(self):
        self.__print_inorder(self.root)
        print()
        self.__print_preorder(self.root)
        print()

    def find(self, v, node):
        if node.v == v:
            print('yes')

        elif node.v > v:
            if node.l:
                self.find(v, node.l)
            else:
                print('no')
        else: # node.v < v:
            if node.r:
                self.find(v, node.r)
            else:
                print('no')

    def __delete_node(self, node):
        if node.l and node.r: # node has two children
            var = node.r
            while var.l:
                var = var.l
            node.v = var.v # this var is the next node when running with inorder
            self.__delete_node(var)
        elif node.l or node.r: # node has a child
            var = node.l if node.l else node.r
            if node.p.v > node.v: # The node is the left child.
                assert node.p.l.v == node.v
                node.p.l = var
                var.p = node.p
                node = None
            else: # The node is the right child.
                assert node.p.r.v == node.v
                node.p.r = var
                var.p = node.p
                node = None
        else: # node has no child
            if node.p.l and node.p.l.v == node.v:
                node.p.l = None
                node = None
            else:
                node.p.r = None
                node = None

    def delete(self, v, node):
        if node.v == v:
            self.__delete_node(node)
        elif node.v > v:
            if node.l:
                self.delete(v, node.l)
            else:
                raise ValueError('key' + str(v) + 'was not found.')
        else: # node.v < v:
            if node.r:
                self.delete(v, node.r)
            else:
                raise ValueError('key' + str(v) + 'was not found.')

    def visualize(self, G, node):
        if node.l:
            G.edge(str(node.v), str(node.l.v))
            self.visualize(G, node.l)
        else:
            G.edge(str(node.v), 'None' + str(node.v))
        if node.r:
            G.edge(str(node.v), str(node.r.v))
            self.visualize(G, node.r)
        else:
            G.edge(str(node.v), 'None' + str(node.v))


def main():
    m = int(input())
    ops = [input().split() for _ in range(m)]
    tree = BinarySearchTree()
    i = 1

    for op in ops:
        if op[0] == 'insert':
            tree.insert(int(op[1]))
        elif op[0] == 'find':
            tree.find(int(op[1]), tree.root)
        elif op[0] == 'delete':
            tree.delete(int(op[1]), tree.root)
        elif op[0] == 'print':
            tree.print()
            # from graphviz import Digraph
            # G = Digraph(format='png')
            # tree.visualize(G, tree.root)
            # G.render("tree"+str(i))
            # i += 1
        else:
            raise ValueError


if __name__ == '__main__':
    main()
