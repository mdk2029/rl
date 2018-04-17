
class DisjoinSet(object) :

    def __init__(self,n):
        self.num = n
        self.parent = [i for i in xrange(self.num)]

    def find(self,n):
        p = self.parent[n]
        if p == n :
            return n
        else :
            ret = self.find(p)
            self.parent[n] = ret
            return ret

    def merge(self,n1,n2):
        n1Guru = self.find(n1)
        n2Guru = self.find(n2)
        if n1Guru != n2Guru :
            self.parent[n1Guru] = n2Guru




