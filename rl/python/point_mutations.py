import base

if __name__ == '__main__' :

    with open('Downloads/rosalind_hamm.txt','r') as fin :
        str1 = fin.readline()
        str2 = fin.readline()

        print base.hamming_distance(str1,str2)
