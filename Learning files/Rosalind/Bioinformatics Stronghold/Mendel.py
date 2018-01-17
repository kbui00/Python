import os
os.system('cls')

def mendel(input):
    k = input[0]    #Homozygous dominant
    m = input[1]    #Heterozygous
    n = input[2]    #Homozygous recessive
    
    return

f = open('rosalind_input.txt','r')
g = open('rosalind_output.txt','w')
print (mendel(f.read()))
#g.write(mendel(f.read()))
g.close()
f.close()
