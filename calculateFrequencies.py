import requests
words = list()

f = open('words.txt', 'r')
words = f.readlines()
f.close()
for i in range(len(words)):
    words[i] = words[i].strip() # remove the newline character  
 
def getFrequency(word):
    return requests.get(f'https://api.datamuse.com/words?sp={word}&md=f&max=1').json()[0]['score']
frequencies = dict()

for word in words:
    data = requests.get(f'https://api.datamuse.com/words?sp={word}&md=f&max=1').json()
    frequencies[word] = {'frequency': data[0]['score'], 'word': data[0]['word']}
    print(f'{word}: {frequencies[word]["frequency"]}')
    
print(frequencies)
