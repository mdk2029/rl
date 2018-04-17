import base

if __name__ == '__main__' :

    genome = ""
    with open('Downloads/dataset_198_3.out', 'w') as fout:
        with open('Downloads/dataset_198_3.txt', 'r') as fin :

            for frag in fin:
                frag = frag.rstrip()
                genome = frag if not genome else genome[:-len(frag)+1] + frag

        fout.write(genome)

