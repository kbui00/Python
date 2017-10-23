#print ("Hello World")
#print ("This isn't a test")
print ("Well this is just the beginning")
c = "weeweewee"[5]
#print (c).upper
c.upper()
#print (len(c))
print ("   Wee   "+" Wiii "+"Woa ")

from datetime import datetime
print (datetime.now())


name = input ('What is your name? ')
color = input ('What is your favorite color? ')
number1 = eval(input ('Enter the first number for operation: '))
number2 = eval(input ('Enter the second number for operation: '))
total = number1 + number2
print ("So your name is %s. Your favorite color is %s, and the sum of the two above numbers is %s" % (name, color, total))
