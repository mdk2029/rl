from fractions import Fraction as Frac

if __name__ == '__main__' :

    k = 29
    m = 24
    n = 22
    T = k+m+n

    prob1 = Frac(k,T) * Frac(k-1,T-1)
    prob2 = Frac(k,T) * Frac(m,T-1)
    prob3 = Frac(k,T) * Frac(n,T-1)
    prob4 = Frac(m,T) * Frac(k,T-1)
    prob5 = Frac(m,T) * Frac(m-1,T-1) * Frac(3,4)
    prob6 = Frac(m,T) * Frac(n,T-1) * Frac(1,2)
    prob7 = Frac(n,T) * Frac(k,T-1)
    prob8 = Frac(n,T) * Frac(m,T-1) * Frac(1,2)

    totalProb = prob1 + prob2 + prob3 + prob4 + prob5 + prob6 + prob7 + prob8
    print float(totalProb)
