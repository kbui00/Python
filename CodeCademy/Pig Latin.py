import os
os.system('cls')

str_input = input('Enter a word: ')
while not str_input.isalpha():
    str_input = input('Please enter a word: ')
word = str_input.lower()
firstword = word[0]
aytail = 'ay.'
translatedword = word.replace(word[0],"")
translatedword = translatedword + firstword + aytail
#A simpler way
#translatedword = word[1:len(word)] + firstword + aytail
print (translatedword)
