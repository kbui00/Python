import os
os.system('cls')

def analyze1(input):
    string1 = input[0]
    string2 = input[1]
    distance = 0
    for i in range(0,len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return str(distance)

def analyze2(input):
    return sum(i != j for i,j in itertools.izip(input[0],input[1]))

f = open('rosalind_input.txt','r')
g = open('rosalind_output.txt','w')
#print(analyze(f.readlines()))
g.write(analyze2(f.readlines()))
f.close()
g.close()
