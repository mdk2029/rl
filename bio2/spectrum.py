import base
import itertools

amino_masses = {
    'G' : 57,
    'A' : 71,
    'S' : 87,
    'P' : 97,
    'V' : 99,
    'T' : 101,
    'C' : 103,
    'I' : 113,
    'L' : 113,
    'N' : 114,
    'D' : 115,
    'K' : 128,
    'Q' : 128,
    'E' : 129,
    'M' : 131,
    'H' : 137,
    'F' : 147,
    'R' : 156,
    'Y' : 163,
    'W' : 186
}

def cyclic_subpeptides(peptide) :

    def subpeptides(peptide) :
        for i in xrange(1,len(peptide)) :
            yield peptide[:i]

    yield ''
    for i in xrange(0,len(peptide)) :
        rotated = peptide[i:] + peptide[:i]
        for res in subpeptides(rotated) :
            yield res

    yield peptide

def cyclospectrum(peptide) :

    res = []

    for c in cyclic_subpeptides(peptide) :
        sum = 0
        for a in c :
            sum += amino_masses[a.upper()]

        res.append(sum)

    return sorted(res)


if __name__ == '__main__' :

    #res = cyclospectrum('LEQN')
    #print ' '.join(str(r) for r in res)

    with open('Downloads/dataset_98_4.txt','r') as fin :
        with open('Downloads/dataset_98_4_out.txt','w') as fout :
            peptide = fin.readline().strip()
            fout.write(' '.join(str(r) for r in cyclospectrum(peptide)))

