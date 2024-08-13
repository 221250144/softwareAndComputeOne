if __name__ == '__main__':
    n = int(input())
    ans, op, x, y = '', '', 0, 0
    for i in range(n):
        read = input().split()
        if len(read) == 3:
            op = read[0]
            x = read[1]
            y = read[2]
        else:
            x = read[0]
            y = read[1]
        if op == 'a':
            ans = x + '+' + y + '=' + str(int(x) + int(y))
        elif op == 'b':
            ans = x + '-' + y + '=' + str(int(x) - int(y))
        else:
            ans = x + '*' + y + '=' + str(int(x) * int(y))
        print(ans)
        print(len(ans))
