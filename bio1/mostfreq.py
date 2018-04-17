from collections import Counter
import sys

def mostFreq(text, size) :
    kmers = []
    for idx in range(0,len(text)-size+1) :
        kmers.append(text[idx:idx+size])

    kmers = Counter(kmers).most_common()
    assert kmers

    maxfreq = kmers[0][1]
    freq_kmers = []
    for k,s in kmers :
        if s == maxfreq :
            freq_kmers.append(k)
        else :
            break

    freq_kmers.sort()
    for k in freq_kmers:
        sys.stdout.write(k)
        sys.stdout.write(' ')
    sys.stdout.write('\n')
    sys.stdout.flush()

        



# if __name__ == '__main__' :
#     f = open('Downloads/dataset_2_9.txt', 'r')
#     text = f.readline().rstrip()
#     print text
#     size = int(f.readline().rstrip())
#     print size
#     print "******"
#     mostFreq(text,size)

if __name__ == '__main__' :
    mostFreq('TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT',3)



