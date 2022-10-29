D = [1,2,3,4,5,6]

s = [x for x in D if D.index(x) % 2 == 1]

print(D, sum(s))
