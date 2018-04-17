

class NextLine(object) :
    def __init__(self,fin):
        self.fin = fin
        self.cached_line = None

    def get_next_line(self):
        if self.cached_line is not None :
            ret = self.cached_line
            self.cached_line = None
            return ret
        else :
            return self.fin.readline()

    def push_next_line(self,line):
        assert not self.cached_line
        self.cached_line = line


def get_next_fasta_input(nl) :
    id = None
    input = ''
    state = 'id'

    while True :
        rline = nl.get_next_line()
        line = rline.strip()
        if not line :
            break
        if state == 'id' :
            if line[0] != '>' :
                continue
            else :
                id = line[1:]
                state = 'dna'
        elif state == 'dna':
            if line[0] == '>' :
                assert input
                nl.push_next_line(rline)
                break
            else :
                input = input + line


    return (id,input)

def dnas_from_file(filename):
    dnas = []
    with open(filename,'r') as fin :
        nl = NextLine(fin)
        while True :
            id,dna = get_next_fasta_input(nl)
            if not id :
                return dnas
            else :
                dnas.append((id,dna))



