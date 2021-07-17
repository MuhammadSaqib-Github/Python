import random
words = ['mango' , 'orange' , 'pakistan' , 'saqib']
index = random.randint(0 , len(words)-1)
word = words[index]
print('random word is ' , word)
word = ''
for i in range(len(words[index])):
    word = word + "*"
print(word)
while True:
    guess = input('enter a guess letter: ')
    if guess in words[index]:
        for i in  len(words[index]):
            if words[index][i]==guess:
                word.remove(i)
                word[i]=guess
                