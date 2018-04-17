import sys
import StringIO

def patternMatch(pattern, genome) :
    plen = len(pattern)
    glen = len(genome)
    positions = []
    for idx in range(0,glen-plen+1) :
        if genome[idx:idx+plen] == pattern :
            positions.append(idx)

    return positions
            


if __name__ == '__main__' :
    f = open('Downloads/dataset_3_5.txt', 'r')
    pattern = f.readline().rstrip()
    genome = f.readline().rstrip()
    positions = patternMatch(pattern, genome)

    buf = StringIO.StringIO()
    for i in positions :
        buf.write("%d " % i)

    print buf.getvalue()

    
    
