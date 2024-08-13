def change(a):
    t = a[::-1]
    return t


if __name__ == '__main__':
    s = input()
    if '.' in s:
        s1, s2 = s.split('.')
        s1, s2 = (change(s1)).lstrip('0'), change(s2).rstrip('0')
        print((s1 if s1 != '' else '0') + '.' + (s2 if s2 != '' else '0'))
    elif '/' in s:
        s1, s2 = s.split('/')
        s1, s2 = (change(s1)).lstrip('0'), change(s2).lstrip('0')
        print((s1 if s1 != '' else '0') + '/' + s2 if s2 != '' else '0')
    elif '%' in s:
        if s[:len(s) - 1] == '0':
            print('0%')
        else:
            s = change(s[:len(s) - 1]).lstrip('0')
            print(s + '%')
    else:
        if s == '0':
            print(0)
        else:
            s = change(s).lstrip('0')
            print(s)
