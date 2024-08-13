import sys
from collections import Counter
from math import sqrt

if __name__ == '__main__':
    s = input()
    num = Counter(s)
    maxn = max(num.values())
    minn = min(num.values())
    ans = maxn - minn
    if ans >= 2:
        for i in range(2, int(sqrt(ans) + 1)):
            if ans % i == 0:
                print("No Answer\n0")
                sys.exit()
        print("Lucky Word\n%d" % ans)
    else:
        print("No Answer\n0")
