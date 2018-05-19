"""
https://onlinejudge.u-aizu.ac.jp/#/courses/lesson/1/ALDS1/5/ALDS1_5_B
"""

import copy


def merge(array, helper, left, mid, right, c):
    helper[left:right+1] = array[left:right+1]

    l_point = left
    r_point = mid + 1
    point = left

    while (l_point <= mid) and (r_point <= right):
        if helper[l_point] > helper[r_point]:
            array[point] = helper[r_point]
            r_point += 1
        else:
            array[point] = helper[l_point]
            l_point += 1
        point += 1

    c += right - left + 1

    remaining = mid - l_point
    array[point:point+remaining+1] = helper[l_point:mid+1]

    return c


def mergesort(array, helper, left, right, c):
    if left < right:
        mid = int((left + right) / 2)
        c = mergesort(array, helper, left, mid, c)
        c = mergesort(array, helper, mid + 1, right, c)
        c = merge(array, helper, left, mid, right, c)
    return c


def main():
    n = int(input())
    array = list(map(int, input().split()))
    helper = copy.deepcopy(array)

    left = 0
    right = n-1

    c = 0
    c = mergesort(array, helper, left, right, c)

    print(' '.join(list(map(str, array))))
    print(c)


if __name__ == '__main__':
    main()
