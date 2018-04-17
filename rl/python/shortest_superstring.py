import itertools
import fasta

def merge(str1,str2) :
    common = 0
    for idx in xrange(1,min(len(str1),len(str2))+1) :
        if str1[len(str1)-idx:] != str2[:idx] :
            continue
        else :
            common = idx

    return str1[:len(str1)-common] + str2

def shortest_superstring_greedy(inputs) :

    def merge_greedy(inputs) :
        merged_max_len = None
        merged_max = None
        idx1_max = None
        idx2_max = None

        inputs_len = len(inputs)
        for idx1 in xrange(inputs_len) :
            for idx2 in xrange(inputs_len) :
                if idx1 != idx2 :
                    merged = merge(inputs[idx1],inputs[idx2])
                    if merged_max_len is None or len(inputs[idx1]) + len(inputs[idx2]) - len(merged)  > merged_max_len :
                        merged_max_len = len(inputs[idx1]) + len(inputs[idx2]) - len(merged)
                        merged_max = merged
                        idx1_max = idx1
                        idx2_max = idx2

        return merged_max,idx1_max,idx2_max

    while len(inputs) != 1 :
        merged_max,idx1,idx2 = merge_greedy(inputs)

        assert idx1 is not None
        assert idx2 is not None

        if idx1 > idx2 :
            del inputs[idx1]
            del inputs[idx2]
        else :
            del inputs[idx2]
            del inputs[idx1]

        inputs.append(merged_max)

    return inputs[0]


def shortest_superstring_brute_force(inputs) :

    def superstring(inputs) :

        assert isinstance(inputs,list)
        assert isinstance(inputs[0],str)

        merged = ''
        for inp in inputs :
            merged = merge(merged,inp)

        return merged

    num_inputs = len(inputs)
    indices = [i for i in xrange(num_inputs)]
    for perm in itertools.permutations(indices) :
        permuted_inputs = [inputs[i] for i in perm]
        ss = superstring(permuted_inputs)
        superstrings.append((ss,len(ss)))

    print min(superstrings, key=lambda elem : elem[1])

if __name__ == '__main__' :

    inputs = []
    superstrings = []
    with open('Downloads/rosalind_long.txt') as fin :
        nl = fasta.NextLine(fin)
        while True:
            id,dna = fasta.get_next_fasta_input(nl)
            if not id :
                break
            inputs.append(dna)


    #shortest_superstring_brute_force(inputs)
    o = shortest_superstring_greedy(inputs)
    with open('Downloads/rosalind_long_out.txt','w') as fout :
        fout.write(o)
        fout.write('\n')







