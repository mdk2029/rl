import fasta

def all_subs(input_str,length) :
    for idx in xrange(len(input_str)-length+1) :
        yield input_str[idx:idx+length]

if __name__ == '__main__':

    dnas = fasta.dnas_from_file('Downloads/rosalind_lcsm.txt')
    dnas = [d for (_,d) in dnas]

    candidate = min(dnas,key=lambda d : len(d))
    dnas.remove(candidate)

    for length in xrange(len(candidate),0,-1):
        for sub in all_subs(candidate,length) :
            success = True
            for d in dnas :
                if not sub in d :
                    success = False
                    break
            if success :
                print sub
                exit(0)



