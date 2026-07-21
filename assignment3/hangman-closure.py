def make_hangman(secret_word):
    
    guesses = []
    answer = set(secret_word)

    def hangman_closure(letter):
        nonlocal guesses
        nonlocal answer
        output = ""
        
        guesses.append(letter)

        for char in secret_word:
            if (char in guesses):
                output = output + char

            else:
                output = output + "_"

        print(output)
        
        for char in answer:
            if char not in guesses:
                return False
        
        return True
    
    return hangman_closure




FOUND = False
word = "Orthodontist"
secret = make_hangman(word)
guess = input("Guess a letter: ")

while (not FOUND):

    FOUND = secret(guess)

    if FOUND:
        print(f"You guessed it! The word was \"{word}\".")
        break

    else:
        guess = input("Guess another letter: ")
    