if __name__ == '__main__':
    s = list(input())
    ans = 0
    for i in s:
        if i != ' ':
            ans += 1
    print(ans)
