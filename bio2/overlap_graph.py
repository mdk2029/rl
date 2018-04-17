import base

def compute_graph(kmers) :

    return [(a,b) for a in kmers for b in kmers if a[1:] == b[:-1] ]



if __name__ == '__main__' :

    with open('Downloads/dataset_198_9_out.txt', 'w') as fout:
        with open('Downloads/dataset_198_9.txt', 'r') as fin :

            #g = compute_graph(["ATGCG","GCATG","CATGC","AGGCA","GGCAT"])

            kmers = []
            for kmer in fin:
                if kmer.find("Input") != -1 :
                    continue
                if kmer.find("Output") != -1:
                    break
                kmers.append(kmer.rstrip())

            g = compute_graph(kmers)
            for e1,e2 in g :
                fout.write(e1)
                fout.write(" -> ")
                fout.write(e2 + "\n")


