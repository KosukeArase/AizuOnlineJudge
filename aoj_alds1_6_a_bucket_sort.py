"""
https://onlinejudge.u-aizu.ac.jp/#/courses/lesson/1/ALDS1/6/ALDS1_6_A
"""


def main():
    n = int(input())
    array = list(map(int, input().split()))

    maximum = 10000

    bucket = [0] * (maximum + 1)

    for x in array:
        bucket[x] += 1

    idx = 0
    for v, c in enumerate(bucket):
        array[idx:idx+c] = [v] * c
        idx += c

    print(' '.join(list(map(str, array))))

if __name__ == '__main__':
    main()
