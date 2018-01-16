import os
os.system('cls')

f = open('rosalind_input.txt', 'r')
g = open('rosalind_output.txt', 'w')
d = {}
string = f.readline()
for i in string.split():
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    g.write(i + ' ' + str(d[i]) + '\n')
f.close()
g.close()
