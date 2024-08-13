if __name__ == '__main__':
    target = input().lower()
    m = ' ' + target + ' '
    t = ' ' + input().lower() + ' '
    s = t.split()
    first, cnt = -1, 0
    for i in range(len(s)):
        if target == s[i]:
            if first == -1:
                first = t.find(m)
            cnt += 1
    if first == -1:
        print(-1)
    else:
        print(cnt, first)
