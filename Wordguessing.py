import random
name = input("What is your name? ")
print("Good Luck ! ", name)
 
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks','hello','python','coding','sameer']
word = random.choice(words)
 
 
print("Guess the characters")
 
guesses = ''
 
# any number of turns can be used here
turns = 12
 
 
while turns > 0:
    failed = 0
    for char in word:
        # comparing that character with the character in guesses
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
 
    if failed == 0:
       
        print("You Win\n")
 
        # this print the correct word
        print("The word is: ", word)
        break
 
    print()
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
 
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
 
        if turns == 0:
            print("You Loose")
