import json
frequencies = dict()
with open('frequencies.json', 'r') as f:
    frequencies = json.loads(f.read())
with open('words.txt', 'r') as f:
    words = f.readlines()
    for i in range(len(words)):
        words[i] = words[i].strip() # remove the newline character
    
from main import Constraint
Constraint.frequencies = frequencies
print(Constraint.highestFrequency(words))

    
