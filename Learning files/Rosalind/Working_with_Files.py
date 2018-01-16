import os
os.system('cls')

f = open('rosalind_input.txt', 'r')
g = open('rosalind_output.txt', 'w')
for i in f.readlines()[1::2]:
    g.write(i)
g.close()
f.close()
