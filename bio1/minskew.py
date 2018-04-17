import sys

def min_skew(patternstr) :
    skews = [0]
    for nucleotide in patternstr :
        if nucleotide == 'G' :
            skews.append(skews[-1] + 1)
        elif nucleotide == 'C' :
            skews.append(skews[-1] - 1)
        else :
            skews.append(skews[-1])

    assert(len(skews) == len(patternstr) + 1)

    minskew = min(skews)
    minindices = []
    for idx,skew in enumerate(skews) :
        if skew == minskew :
            minindices.append(idx)

    return minindices

if __name__ == '__main__' :
    #minindices = min_skew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')
    #map(lambda x : sys.stdout.write("%d " % x) , minindices)
    with open("Downloads/minimum_skew_data.txt", 'r') as f :
        f.readline()
        input = f.readline().rstrip()
        minindices = min_skew(input)
        map(lambda x : sys.stdout.write("%d " % x), minindices)

