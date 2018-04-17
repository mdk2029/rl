import itertools

if __name__ == '__main__' :

    n = 5

    l = [i for i in xrange(1,1+n)]
    product = 1
    for num in l :
        product *= num

    with open('Downloads/permutations_out.txt','w') as fout :

        fout.write(str(product))
        fout.write('\n')

        for p in itertools.permutations(l) :
            fout.write(' '.join([str(i) for i in p]))
            fout.write('\n')

        fout.write('\n')




