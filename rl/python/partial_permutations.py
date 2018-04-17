from operator import mul

def npk(n,k) :
    assert k <= n

    return reduce(mul, [n-k+i for i in xrange(1,k+1)], 1)


if __name__ == '__main__' :

    n = 91
    k = 9

    print npk(n,k) % 1000000
