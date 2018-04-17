import sys
import freqArray
from collections import defaultdict

__all__ = ['ClumpFinding']



def ClumpFinding(genome,k,L,t):

    globalfA = freqArray.initializeFreqArray(k)

    #compute fA for initial L window
    windowfA_list = freqArray.computingFrequencies(genome[0:L],k)

    #convert to dict
    windowfA = defaultdict(int)
    for (i,freq) in enumerate(windowfA_list) :
        if freq > 0 :
            windowfA[i] = freq

    for (i,freq) in windowfA.iteritems() :
        assert(freq > 0)
        if(freq >= t) :
            globalfA[i] += 1


    #now adjust windowfA
    for idx in xrange(0,len(genome)-L) :
        kmertoremove = freqArray.patternToNumber(genome[idx:idx+k])
        assert kmertoremove in windowfA
        if windowfA[kmertoremove] == 1 :
            windowfA.pop(kmertoremove)
        else :
            windowfA[kmertoremove] -= 1
        kmertoadd = freqArray.patternToNumber(genome[ idx+1+L-k : idx+1+L])
        windowfA[kmertoadd] += 1

        for (i,freq) in windowfA.iteritems() :
            assert(freq > 0)
            if freq >= t :
                globalfA[i] += 1


    ret = []
    for idx,f in enumerate(globalfA):
        if f > 0 :
            ret.append(freqArray.numberToPattern(idx,k))

    return ret

if __name__ == '__main__' :
    clumps = ClumpFinding('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA',5,50,4)
    assert(clumps == ['CGACA','GAAGA'])

    with open('Downloads/dataset_4_5.txt', 'r') as f :

        genome = f.readline().rstrip()
        params = f.readline().rstrip()
        plist = params.split()
        k = int(plist[0])
        L = int(plist[1])
        t = int(plist[2])

        print genome
        print k,L,t

        clumps = ClumpFinding(genome,k,L,t)
        print clumps

        for c in clumps:
            sys.stdout.write(c)
            sys.stdout.write(" ")




