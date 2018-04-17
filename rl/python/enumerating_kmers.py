

if __name__ == '__main__':

    s = 'IWBQSY'
    strs = []
    with open('Downloads/rosalind_lexf_out.txt','w') as fout :
        for c1 in s :
            for c2 in s :
                for c3 in s:
                    strs.append(c1+c2+c3)


        for s in sorted(strs) :
            fout.write(s)
            fout.write('\n')
