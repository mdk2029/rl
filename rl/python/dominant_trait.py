

# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa

prob_list = [ 1.0, 1.0, 1.0, .75, .5, 0 ]

#couples_count = [1,0,0,1,0,1]
couples_count = [18230, 18342, 18611, 17044, 19943, 19814]


expected = 0.0

for i in xrange(6) :
    expected += couples_count[i] * 2 * prob_list[i]

print expected
