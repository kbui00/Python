import os
os.system('cls')

def rabinacci(input):
    months = int(input[0])
    rate = int(input[1])
    total = 0
    if months == 1:
        total = 1
    elif months == 2:
        total = 1
    elif months <= 4:
        total = 1 + rate
    else:
        


f = open('rosalind_input.txt', 'r')
g = open('rosalind_output.txt', 'w')
g.write(rabinacci(f.read().split()))


f.close()
g.close()
