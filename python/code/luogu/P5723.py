from math import sqrt


def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    num = int(input())
    Prime = list()
    a = 0
    number = 0
    while True:
        if isprime(number):
            Prime.append(number)
            a += number
        if a > num:
            Prime.remove(number)
            break
        number += 1
    for i in Prime:
        print(i)
    print(len(Prime))
