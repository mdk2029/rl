import urllib2
import fasta
import re

glycosylation = r'(?=N[^P][ST][^P])'

def find_glyco_loc(protein) :
    matches = re.finditer(glycosylation,protein)
    return [match.start()+1 for match in matches]


if __name__ == '__main__' :

    with open('Downloads/rosalind_mprt.txt','r') as fin:
        with open('Downloads/rosalind_mprt_out.txt','w') as fout:

            for line in fin :
                id = line.strip()
                if id :
                    response = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % id).read()
                    response = response.split('\n')
                    protein = ''.join(response[1:])
                    locations = find_glyco_loc(protein)
                    if locations :
                        fout.write(id)
                        fout.write('\n')
                        fout.write(' '.join([str(i) for i in locations]))
                        fout.write('\n')






