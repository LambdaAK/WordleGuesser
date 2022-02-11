def game():
    turn = 0
    word = "crane"
    while True:
        guess = input("Guess: ")
        if word == guess:
            print('you win!')
            return True
        result = [] # index is the letter index, value is the result/color of the letter
        for i in range(5):
            letter = guess[i]
            # gray
            if letter not in word:
                result.append(0)
            # yellow or green
            elif letter in word:
                if word[i] != letter:
                    result.append(1)
                else:
                    result.append(2)
        print(result)
        turn += 1
        if turn == 6:
            print('you lose!')
            return False
        

        

    