import os
os.system('cls')

f = open('rosalind_input.txt', 'r')
g = open('rosalind_output.txt', 'w')
s = f.readline()
g.write("%d %d %d %d" % (s.count("A"),s.count("C"),s.count("G"),s.count("T")))
f.close()
g.close()
