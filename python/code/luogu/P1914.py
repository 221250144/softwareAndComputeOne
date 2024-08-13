if __name__ == '__main__':
    n = int(input())
    s = input()
    old = list(s)
    new = list()
    for i in old:
        new.append(chr(ord(i) + n if ord(i) + n <= 122 else ord(i) + n - 26))
    print(''.join(new))
