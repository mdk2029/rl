import itertools
import math

def signed_seq(seq) :

    assert seq
    assert isinstance(seq, list)
    assert isinstance(seq[0],int)

    if len(seq) == 1 :
        return [[seq[0]],[-seq[0]]]
    else :
        return [ [seq[0]] + perm for perm in signed_seq(seq[1:]) ] + [ [-seq[0]] + perm for perm in signed_seq(seq[1:]) ]


def signed_perm( seq ) :

    assert seq
    assert isinstance(seq, list)
    assert isinstance(seq[0],int)

    for perm in itertools.permutations(seq) :
        for s in signed_seq(list(perm)) :
            yield s



if __name__ == '__main__' :
    #print signed_perm([1])
    #print signed_perm([1,2])
    #print signed_perm([1,2,3])

    n = 3

    with open('Downloads/signed_perms_out.txt','w') as fout:
        fout.write(str(math.factorial(n) * pow(2,n)))
        fout.write('\n')
        for x in signed_perm([1,2,3]) :
            fout.write(' '.join([str(i) for i in x]))
            fout.write('\n')
        fout.write('\n')




