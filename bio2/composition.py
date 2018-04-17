import base
import time

if __name__ == '__main__' :


    f = open('Downloads/dataset_197_3.txt', 'r')
    k = int(f.readline().rstrip())
    dna = f.readline().rstrip()

    target = open('Downloads/dataset_197_3_out.txt','w')

    for k1 in base.kmers(dna,k):
        print k1

    for k in base.kmers(dna,k) :
        target.write(k)
        target.write('\n')

    target.close()
    time.sleep(3)

