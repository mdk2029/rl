from base import complement

if __name__ == '__main__' :
    #f = open('Downloads/dataset_3_2.txt','r')
    #strand = f.readline().rstrip()
    strand = 'TTGTGTC'
    assert complement(strand) == 'GACACAA'
    
