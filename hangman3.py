words = ["python", "java", "program", "variable", "string"]  # word list
score = 0

print("🎮 Welcome to Hangman!")

for word in words:   # loop through each word in the list
    guessed = []
    attempts = 6

    print("\nNew word to guess:")
    print("_ " * len(word))  # using the len function

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.")
            continue

        if guess in guessed:
            print(" Already guessed!")
            continue

        guessed.append(guess)  # add to guessed letters

        if guess in word:
            print(" Correct!")
        else:
            print(" Wrong!")
            attempts -= 1
            print("Attempts left:", attempts)

        # Display progress
        progress = " ".join([ch if ch in guessed else "_" for ch in word])
        print(progress)

        # -------- Simpler win check (replaces all(...)) --------
        won = True
        for ch in word:
            if ch not in guessed:
                won = False
                break

        if won:
            print(" You win! The word was:", word)
            score += 1
            break
        # -------------------------------------------------------

    else:
        print(" You lose! The word was:", word)

print("\n Game Over! You played all words.")
print(" Final Score:", score, "/", len(words))
