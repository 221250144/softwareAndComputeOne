import math

prime = []


def produce():
    for i in range(2, 201):
        t = 2
        judge = 0
        while t <= math.sqrt(i):
            if i % t == 0:
                judge = 1
                break
            t += 1
        if judge == 0:
            prime.append(i)


if __name__ == '__main__':
    produce()
    ans = [[0 for i in range(201)] for j in range(201)]
    ans
