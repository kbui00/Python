import os
os.system('cls')

def reading(listinput):
    dictionary = {}
    for i in listinput:
        if i[0] == '>':
            key = i.lstrip('>')
            dictionary [key] = ''
        else:
            dictionary [key] += i.rstrip('\n')
    return dictionary

def analyze(dictinput):
    totallist = dictinput
    percentgc = 0
    highestkey = 0
    highestvalue = 0
    for i in totallist:
        percentgc = (totallist[i].count('G') + totallist[i].count('C')) / len(totallist[i])
        totallist [i] = percentgc*100
    highestvalue = max(totallist.values())
    highestkey = max([[totallist[key],key] for key in totallist])[1]
    return "%s%f" % (highestkey, highestvalue)

f = open('rosalind_input.txt','r')
g = open('rosalind_output.txt','w')
g.write(analyze(reading(f.readlines())))
f.close()
g.close()
