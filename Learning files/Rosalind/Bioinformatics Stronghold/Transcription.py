import os
os.system('cls')

f = open('rosalind_input.txt', 'r')
g = open('rosalind_output.txt', 'w')

s = f.read()
g.write(s.replace('T', 'U'))

f.close()
g.close()
