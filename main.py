from json import loads
import os
from statistics import NormalDist
NOT = 0 # the character doesn't exist in the word
ELSE = 1 # the character exists in the word, but at another index
RIGHT = 2 # the character exists in the word, and at the right index
GRAY = '⬛'
YELLOW = '🟨'
GREEN = '🟩'
WHITE = '⬜'
BLUECODE = '\033[2;34m'
GREENCODE = '\033[2;32m'
YELLOWCODE = '\033[1;33m'


forbiddenLetters = []


class Constraint:
    words = list()
    frequencies = dict()
    @classmethod
    def loadwords(cls):
        f = open('words.txt', 'r')
        cls.words = f.readlines()
        f.close()
        for i in range(len(cls.words)):
            cls.words[i] = cls.words[i].strip() # remove the newline character
        f = open('frequencies.json', 'r')
        cls.frequencies = loads(f.read())
        f.close()
    
    
    def __init__(self, letter0, letter1, letter2, letter3, letter4, val0, val1, val2, val3, val4):
        # make an attribute for each argument to the contructor
        self.letter0 = letter0
        self.letter1 = letter1
        self.letter2 = letter2
        self.letter3 = letter3
        self.letter4 = letter4
        self.val0 = val0
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3
        self.val4 = val4
        
        if self.val0 == NOT:
            forbiddenLetters.append(self.letter0)
        if self.val1 == NOT:
            forbiddenLetters.append(self.letter1)
        if self.val2 == NOT:
            forbiddenLetters.append(self.letter2)
        if self.val3 == NOT:
            forbiddenLetters.append(self.letter3)
        if self.val4 == NOT:
            forbiddenLetters.append(self.letter4)
        print(forbiddenLetters)
        
    @classmethod 
    def checkWord(cls, word, constraints) -> bool:
        '''
        if there is a forbidden letter in the word, return False
        if there is a letter that exists, but at a different index (yellow)
            if the letter is at the forbidden index, return False
            if the letter exists elsewhere, return True
            else return False
        if there is a letter that exists at a specific index, but isn't present there, return False
        
        End, return True
        '''
        
        # gray
        for i in range (len(constraints)):
            for letter in word:
                if letter in forbiddenLetters:
                    return False
            
        # check if the word exists but should be in another place
        # yellow
        for i in range(len(word)):
            for constraint in constraints:
                # access the correct property based on i, the index of the letter in the word
                if i == 0:
                    if constraint.letter0 == word[i] and constraint.val0 == ELSE:
                        return False
                    # make sure the character exists somewhere else in the word
                    if constraint.letter0 not in word and constraint.val0 == ELSE:
                        return False
                if i == 1:
                    if constraint.letter1 == word[i] and constraint.val1 == ELSE:
                        return False
                    if constraint.letter1 not in word and constraint.val1 == ELSE:
                        return False
                if i == 2:
                    if constraint.letter2 == word[i] and constraint.val2 == ELSE:
                        return False
                    if constraint.letter2 not in word and constraint.val2 == ELSE:
                        return False
                if i == 3:
                    if constraint.letter3 == word[i] and constraint.val3 == ELSE:
                        return False
                    if constraint.letter3 not in word and constraint.val3 == ELSE:
                        return False
                if i == 4:
                    if constraint.letter4 == word[i] and constraint.val4 == ELSE:
                        return False
                    if constraint.letter4 not in word and constraint.val4 == ELSE:
                        return False
                        
                # green
                # check if there is a RIGHT letter anywhere at this spot for any constraint. 
                # If there is, return False if the letter isn't present in word at the right index
                if i == 0:
                    if constraint.letter0 != word[i] and constraint.val0 == RIGHT: # if the letter is not the same as the word, and it's a RIGHT letter
                            return False
                if i == 1:
                    if constraint.letter1 != word[i] and constraint.val1 == RIGHT: # if the letter is not the same as the word, and it's a RIGHT letter
                            return False
                if i == 2:
                    if constraint.letter2 != word[i] and constraint.val2 == RIGHT: # if the letter is not the same as the word, and it's a RIGHT letter
                            return False
                if i == 3:
                    if constraint.letter3 != word[i] and constraint.val3 == RIGHT: # if the letter is not the same as the word, and it's a RIGHT letter
                            return False
                if i == 4:
                    if constraint.letter4 != word[i] and constraint.val4 == RIGHT: # if the letter is not the same as the word, and it's a RIGHT letter
                            return False
                                
        return True
    
    @classmethod
    def highestFrequency(cls, words: list):
        highestValue = 0
        highestWord = str()
        if len(words) == 0:
            print('no words found')
            return
        for word in words:
            if cls.frequencies[word]['frequency'] > highestValue:
                highestValue = cls.frequencies[word]['frequency']
                highestWord = word
        return highestWord
        
       
    @classmethod
    def calculateGuess(cls, constraints: list):
        guesses = []
        for word in cls.words:
            if cls.checkWord(word, constraints): # if the word passes the constraints
                guesses.append(word)
                
        return guesses # returns all valid guesses
    
clear = lambda: os.system('cls')    

guessSquares = []
def printGuessSquares():
    '''Prints the board with the guesses'''
    if len(guessSquares) == 0:
        return
    for row in guessSquares:
        print(row)
    # print more white squares up to 6 columns
    for i in range(len(guessSquares), 6):
        for j in range(5):
            print(WHITE, end='')
        print()
    
        
def _input(prompt: str):
    '''A formatted input function'''
    print(GREENCODE)
    result = input(prompt)
    print(BLUECODE)
    clear()
    return result


def instructions():
    print('''
        For each guess, input your chosen word.
        Afterwards, input the data from the guess.
            gray = 0
            yellow = 1
            green = 2
        
    ''')

def main():
    
    firstRound = True
    Constraint.loadwords()
    constraints = list()
    print(f'The optimal guess is\n-----\n{YELLOWCODE}crane{BLUECODE}\n-----')
    word = 'crane' # start with crane. It's the best first word
    instructions()
    while True: 
        word = str()
        validChars = False
        word = str()
        while len(word) != 5 and not validChars:
            word = _input('Enter your guess: ')
            if len(word) != 5:
                print('Guess length must be 5')
            
            validChars = True
            for letter in word:
                if letter not in 'abcdefghijklmnopqrstuvwxyz':
                    validChars = False
                    print('Guess must be all lowercase letters')
            
        result = str()
        validChars = False
        while len(result) != 5 and not validChars:
            result = _input('Enter the result of the guess: ')
            if len(result) != 5:
                print('Result length must be 5')
            
            # set to True, then set back to False if there's in invalid character
            validChars = True
            for letter in result:
                if letter not in '012':
                    validChars = False
                    print('Results must be a number between 0 and 2')
            
        result0 = int(result[0])
        result1 = int(result[1])
        result2 = int(result[2])
        result3 = int(result[3])
        result4 = int(result[4])
        
        # add the new constraint
        constraints.append(Constraint(word[0], word[1], word[2], word[3], word[4], result0, result1, result2, result3, result4))
        possible: list = Constraint.calculateGuess(constraints)
        optimal: str = Constraint.highestFrequency(possible)
        if optimal == None:
            print('No words found')
            return
        squares = ''
        for letter in result:
            letter = int(letter)
            if letter == NOT:
                squares += GRAY
            elif letter == ELSE:
                squares += YELLOW
            else:
                squares += GREEN
        guessSquares.append(squares)
        clear()
        printGuessSquares()
        print(f'The optimal guess is\n-----\n{YELLOWCODE}{optimal}{BLUECODE}\n-----')
        
        
def mainWrapper():
    while True:
        main()
        

if __name__ == '__main__':
    clear()
    print(BLUECODE)
    mainWrapper()
