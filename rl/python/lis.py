import operator

def lis(seq) :
    seqlen = len(seq)
    L = [1] * seqlen
    P = [i for i in xrange(seqlen)]

    for i in xrange(seqlen) :
        li = L[i]
        pi = P[i]
        for j in xrange(i) :
            if seq[j] < seq[i] and L[j] + 1 > li :
                li += 1
                pi = j
        L[i] = li
        P[i] = pi

    idx,_ = max(enumerate(L),key=operator.itemgetter(1))

    path = []
    while P[idx] != idx :
        path.insert(0,seq[idx])
        idx = P[idx]
    path.insert(0,seq[idx])

    return path


if __name__ == '__main__' :

    seq = []

    with open('Downloads/rosalind_lgis.txt','r') as fin :
        n = fin.readline().strip()
        seq = fin.readline().split()
        assert len(seq) == int(n)
        seq = [int(s) for s in seq]

        with open('Downloads/rosalind_lgis_out.txt','w') as fout:
            increasing = lis(seq)
            fout.write(' '.join([str(i) for i in increasing]))
            fout.write('\n')

            decreasing = lis([elem for elem in reversed(seq)])
            fout.write(' '.join([str(i) for i in reversed(decreasing)]))
            fout.write('\n')




