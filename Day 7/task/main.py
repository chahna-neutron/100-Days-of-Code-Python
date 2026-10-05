import random


import hangman_words # or we can also use from hangman_words import word_list
import hangman_art                     # this we use to import specifically imported the word_list.

lives = 6
print(hangman_art.logo)


chosen_word = random.choice(hangman_words.word_list)# when we use  that we can use use
print(chosen_word)                                    #random.choice(words_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    if guess in  correct_letters:
        print("You have already guessed this letter!", guess)
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)




    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word!")
        lives -= 1

        if lives == 0:
            game_over = True


            print(f"***********************IT WAS {chosen_word} ! , YOU LOSE****************************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(hangman_art.stages[lives])
