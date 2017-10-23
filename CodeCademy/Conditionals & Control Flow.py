#bool_1 = 5 > 3 and 2 < 1
#print (bool_1)

def testing():
    print ("sdjsd")
    print ("")
testing()

x = input('Enter a list of numbers with space between each: ')
#a = eval(input('How many items do you want to convert to numbers? '))
lst1 = x.split()
lst2 = []
for b in range(0,len(lst1)):
    lst2.append(int(lst1[b]))
    #print (lst2)
print (lst2)
lst1 = [int(a) for a in lst1]
print (lst1)
def smallestvalue(lst2):
    print (min(lst2))
    return min(lst2)

print ('Sum of the smallest value and 5 is:',smallestvalue(lst2)+5)
