import sys
import base
from spectrum import amino_masses

masses = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
amino_acids_dict = {
    57 : 'G',
    71 : 'A',
    87 : 'S',
    97 : 'P',
    99 : 'V',
    101 : 'T',
    103 : 'C',
    113 : '[IL]',
    114 : 'N',
    115 : 'D',
    128 : '[KQ]',
    129 : 'E',
    131 : 'M',
    137 : 'H',
    147 : 'F',
    156 : 'R',
    163 : 'Y',
    186 : 'W'
}

masses_dict = {
    'G' : 57,
    'A' : 71,
    'S' : 87,
    'P' : 97,
    'V' : 99,
    'T' : 101,
    'C' : 103,
    'I' : 113,
    'L' : 113,
    'N' : 114,
    'D' : 115,
    'K' : 128,
    'Q' : 128,
    'E' : 129,
    'M' : 131,
    'H' : 137,
    'F' : 147,
    'R' : 156,
    'Y' : 163,
    'W' : 186
}

def expand(candidates) :
    return [c + [m] for c in candidates for m in masses]

def linear_spectrum(peptide):
    spectrum = []
    for beg in xrange(0,len(peptide)) :
        for end in xrange(beg+1,len(peptide)+1) :
            pep = peptide[beg:end]
            spectrum.append(sum(pep))

    return spectrum

def is_consistent(subpeptide_spectrum, peptide_spectrum) :
    new_ps = list(peptide_spectrum)
    for s in subpeptide_spectrum :
        if s not in new_ps :
            return False
        new_ps.remove(s)
    return True

def cyclopeptide_sequencing(spectrum) :
    parentmass = spectrum[-1]
    candidates = [[]]
    solutions = []
    while candidates :
        candidates[:] = expand(candidates)
        candidates[:] = [c for c in candidates if is_consistent(linear_spectrum(c),spectrum)]
        remaining_candidates = []
        for c in candidates :
            if sum(c) == parentmass :
                solutions.append(c)
            else :
                remaining_candidates.append(c)
        candidates = remaining_candidates

    return solutions



if __name__ == '__main__' :
    #print linear_spectrum([1,2,3,4])
    #print linear_spectrum2([1,2,3,4])

    #cyclopeptide_sequencing([0,113,128,186,241,299,314,427])

    # spectrum =  [0, 71, 101, 113, 131, 184, 202, 214, 232, 285, 303, 315, 345, 416]
    # solutions = cyclopeptide_sequencing(spectrum)
    #
    # for s in solutions :
    #         sys.stdout.write('-'.join([str(amino_acids_dict[m]) for m in s]))
    #         sys.stdout.write('\n')



    spectrum = [0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333]
    for subpeptide in ['QCV','TCQ','TCE','AQV','VAQ','CTV'] :
        s = [amino_masses[c] for c in subpeptide]
        ls = linear_spectrum(s)
        print is_consistent(ls,spectrum)






    # with open('Downloads/dataset_100_6.txt','r') as fin :
    #     spectrum = [int(i) for i in fin.readline().split()]
    #     solutions = cyclopeptide_sequencing(spectrum)
    #
    #     for s in solutions :
    #         sys.stdout.write('-'.join([str(i) for i in s]))
    #         sys.stdout.write(' ')
    #
    #     sys.stdout.flush()



