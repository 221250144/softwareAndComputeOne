if __name__ == '__main__':
    read = input().split('\n\r')
    a, b = list(), list()
    first, second = -1, -1
    for i in range(len(read)):
        if read[i] == 'EOF':
            if first == -1:
                first = i
            else:
                second = i
    a = read[0:first]
    b = read[first + 1:second]
    print(a, b)
