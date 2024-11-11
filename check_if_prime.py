import math


def is_prime(a):
    x = True

    # 排除小于2的数，2是素数
    if a <= 1:
        print("not prime")
        return

    # 2 是素数
    if a == 2:
        print("prime")
        return

    # 排除偶数和3的倍数
    if a % 2 == 0 or a % 3 == 0:
        print("not prime")
        return

    # 只检查到 sqrt(a)，并且只检查形如 6k ± 1 的数
    for i in range(5, int(math.sqrt(a)) + 1, 6):  # 5, 11, 17, 23, ...
        if a % i == 0 or a % (i + 2) == 0:  # 检查 i 和 i + 2（即 5 和 7, 11 和 13）
            print("not prime")
            return

    print("prime")

