# 유클리드 호제법
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


print(gcd(24, 8))


def lcm(x, y):
    return int(x*y/gcd(x, y))


print(gcd(576, 128))
print(lcm(576, 128))
