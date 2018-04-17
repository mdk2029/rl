
def count(n) :

    assert n % 2 == 0

    return 1 if n == 2 else n/2 * count(n-2)


if __name__ == '__main__' :

    inp = 'CCCUCACACUGGUUAGGGGCGCUAGUUAGCUGACUUGGGUUCGCAGUUCUUGAAACGCGGCACGAAAACAUUCACUAA'

    a = sum(1 if char=='A' else 0 for char in inp)
    u = sum(1 if char=='U' else 0 for char in inp)
    g = sum(1 if char=='G' else 0 for char in inp)
    c = sum(1 if char=='C' else 0 for char in inp)

    assert a == u and g == c

    print count(2*a) * count(2*g)


