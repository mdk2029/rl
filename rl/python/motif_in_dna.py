
def locations(dna,motif) :
    locs = []
    for idx in xrange(0,len(dna)-len(motif)+1) :
        if dna[idx:idx+len(motif)] == motif :
            locs.append(idx+1) #as per spec of problem, indices start with 1

    return locs

if __name__ == '__main__':

    #ret = locations('GATATATGCATATACTT','ATAT')
    with open('Downloads/rosalind_subs.txt','r') as fin:
        dna = fin.readline().strip()
        motif = fin.readline().strip()
        ret = locations(dna,motif)
        print ' '.join([str(i) for i in ret])