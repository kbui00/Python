import os
os.system('cls')

def dnacomplimentary(dna):
    complimentary = {'A':'T','C':'G','G':'C','T':'A'}
    newseq = ''.join(complimentary[i] for i in dna)
    return newseq[::-1]

f = open('rosalind_input.txt', 'r')
g = open('rosalind_output.txt', 'w')
g.write(dnacomplimentary(f.read().rstrip()))
f.close()
g.close()
