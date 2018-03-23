word ='letters'
letter_count = {letter:word.count(letter) for letter in word}
print(letter_count)

print('--------------')

#print(set(word))

ss= set(word)
letter_count = {letter:word.count(letter) for letter in ss}
print(letter_count)
