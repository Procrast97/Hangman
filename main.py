import random

with open("Words/Hangman_wordbank", "r") as f:
    words = f.read()

game = True
word_list = words.split(", ")

def end_game(won):
    if won:
        user_answer = input("You win!, would you like to play again? (y/n): ")
        if user_answer.lower() == "y":
            answer =  True
        else:
            answer =  False
        return answer
    else:
        user_answer = input("You lose!, would you like to play again? (y/n): ")
        if user_answer.lower() == "y":
            answer =  True
        else:
            answer = False
        return answer

while game:
    lives = 10
    curr_word = random.choice(word_list)
    print(curr_word)
    length_of_word = len(curr_word)
    word_to_guess = "_" * length_of_word
    guessed_letters = []
    print(f"Guess the word, there are {length_of_word} letters.")
    while lives > 0:
        if word_to_guess == curr_word:
            if end_game(True):
                game = True
                break
            else:
                game = False
                break
        else:
            print(f"Chances left: {lives}")
            print(f"Word: {word_to_guess}")
            users_guess = input("Guess a letter: ")
            if any(char.isdigit() for char in users_guess) or any(not char.isspace() and not char.isalnum() for char in users_guess) or len(users_guess) > 1:
                print("Please only enter one letter/no symbols/no numbers.")
            else:
                user_guess = users_guess.lower()
                if user_guess in curr_word and user_guess not in word_to_guess:
                    guessed_letters.append(user_guess)
                    print(guessed_letters)
                    print("checked")
                    # for letter in curr_word:
                    letters_list = list(word_to_guess)
                    for i, char in enumerate(curr_word):
                        if char == user_guess:
                            letters_list[i] = user_guess
                    word_to_guess = "".join(letters_list)
                        # word_to_guess = word_to_guess.replace(word_to_guess[curr_word.index(letter)], users_guess)
                else:
                     lives -= 1

    if lives == 0:
        if end_game(False):
            game = True
        else:
            break
    # else:

















