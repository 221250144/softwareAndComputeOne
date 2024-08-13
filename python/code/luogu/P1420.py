if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    m = 0
    index = 0
    while index < n - 1:
        while index < n - 1 and a[index + 1] == a[index] + 1:
            ans += 1
            index += 1
        index += 1
        m = max(m, ans)
        ans = 1
    print(m)
