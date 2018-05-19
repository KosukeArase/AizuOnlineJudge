"""
https://onlinejudge.u-aizu.ac.jp/#/courses/lesson/1/ALDS1/9/ALDS1_9_C
"""

import math


class Heap():
    def __init__(self, length):
        self.values = [None] * length
        self.last = 0

    def __swap(self, i, j):
        self.values[i], self.values[j] = self.values[j], self.values[i]

    def insert(self, v):
        # self.values.append(v)
        self.last += 1
        self.values[self.last] = v

        ind = self.last

        while ind > 1:
            parent = math.floor(ind/2)
            if self.values[parent] < self.values[ind]:
                self.__swap(parent, ind)
                ind = parent
            else:
                break

    def extract(self):
        max_value = self.values[1] # [0] is the dummy
        self.__swap(1, self.last) # move the last value to 1st

        self.values[self.last] = None # remove the last value, equal to pop()
        self.last -= 1

        ind = 1

        while True:
            left = ind * 2
            right = ind * 2 + 1
            size = self.last
            # print(ind, self.values[:5])
            if left <= size and right <= size:
                larger = left if self.values[left] > self.values[right] else right
                if self.values[larger] > self.values[ind]:
                    self.__swap(ind, larger)
                    ind = larger
                else:
                    break
            elif left <= size:
                if self.values[left] > self.values[ind]:
                    self.__swap(ind, left)
                    ind = left
                else:
                    break
            else:
                break
        return max_value


def main():
    max_ops = 2000000
    ops = [None] * max_ops
    length = 1

    for i in range(max_ops):
        op = input().split()
        ops[i] = op
        if op[0] == 'end':
            break
        if op[0] == 'insert':
            length += 1

    heap = Heap(length)

    for op in ops:
        if op[0] == 'insert':
            heap.insert(int(op[1]))
        elif op[0] == 'extract':
            var = heap.extract()
            print(var)
        elif op[0] == 'end':
            break
        else:
            raise ValueError('Invalid operation: {}'.format(op[0]))


if __name__ == '__main__':
    main()
