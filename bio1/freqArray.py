import sys
from base import numberToPattern,patternToNumber

__all__ = ['computingFrequencies', 'initializeFreqArray']

def initializeFreqArray(k) :
    return [ 0 for d in xrange(0,pow(4,k))]


def computingFrequencies(genome, length) :
    freqArray = initializeFreqArray(length)

    for idx in xrange(0, len(genome)-length+1):
        freqArray[patternToNumber(genome[idx:idx+length])] += 1

    return freqArray

if __name__ == '__main__' :
    assert patternToNumber('ATGCAA') == 912
    assert patternToNumber('T') == 3
    assert patternToNumber('AT') == 3
    assert patternToNumber('CCG') == 22

    assert numberToPattern(3,1) == 'T'
    assert numberToPattern(3,2) == 'AT'
    assert numberToPattern(22,3) == 'CCG'
    assert numberToPattern(912,6) == 'ATGCAA'

    assert numberToPattern(5437,7) == 'CCCATTC'
    assert numberToPattern(5437,8) == 'ACCCATTC'

    fA = computingFrequencies('ACGCGGCTCTGAAA',2)
    assert fA == [2,1,0,0,0,0,2,2,1,2,1,0,0,1,1,0]

    f = open('Downloads/dataset_2994_5.txt', 'r')
    genome = f.readline().rstrip()
    length = int(f.readline().rstrip())

    fA = computingFrequencies(genome,length)
    e = ''
    for f in fA:
        e += str(f)
        e += ' '
    e = e.rstrip()

    print e