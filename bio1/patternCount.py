
def patternCount(text,pattern) :
    count = 0
    tlen = len(text)
    plen = len(pattern)

    for idx in range(0,tlen-plen+1) :
        if text[idx:idx+plen] == pattern :
            count = count + 1

    return count

if __name__ == '__main__' :
    # f = open('Downloads/dataset_2_6.txt', 'r')
    # text = f.readline().rstrip()
    # print text
    # pattern = f.readline().rstrip()
    # print pattern
    # print patternCount(text,pattern)
    # print patternCount('GCGCG','GCG')
    print patternCount('CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC','CGCG')
