if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = sum(a[1:n - 1])
    print('%.2f' % (b / (n - 2)))
