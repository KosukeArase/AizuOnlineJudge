"""
https://onlinejudge.u-aizu.ac.jp/#/courses/lesson/1/ALDS1/6/ALDS1_6_C
"""


def partition(array, left, right):
    pivot = array[int((left+right)/2)]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    assert abs(left - right) <= 2
    return left


def quicksort(array, left, right):
    ind = partition(array, left, right)
    if left < ind - 1:
        quicksort(array, left, ind - 1)
    if ind < right:
        quicksort(array, ind, right)


def main():
    n = int(input())
    array = list(map(int, input().split()))

    quicksort(array, 0, n-1)

    print(' '.join(list(map(str, array))))


if __name__ == '__main__':
    main()
