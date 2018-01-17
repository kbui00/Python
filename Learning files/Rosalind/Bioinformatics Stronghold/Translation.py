import os
os.system('cls')

def readtable(input):
    rna = ['A','U','C','G']
    proteindict = {}
    key = ''
    for i in input:
        split = i.split()
        for j in split:
            if j[0] in rna:
                key = j
                proteindict[j] = ''
            else:
                proteindict[key] = j
    return proteindict

def translate(table, seq):
    protein = ''
    codon = ''
    for i in seq:
        codon += i
        if len(codon) > 3:
            if codon in table.keys():
                protein += 
    return

f = open('rosalind_input.txt','r')
h = open('translation_table.txt','r')
g = open('rosalind_output.txt','w')
print (readtable(h.readlines()))

h.close()
g.close()
f.close()
