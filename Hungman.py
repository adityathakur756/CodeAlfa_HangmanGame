import random


# =========================================================
#                  HANGMAN
#              CodeAlpha - Task 1
# =========================================================


# ---------------------------------------------------------
# WORD LIST
# ---------------------------------------------------------

words = {
    "easy": [
        {
            "word": "python",
            "hint": "A popular programming language"
        },
        {
            "word": "laptop",
            "hint": "A portable computer"
        },
        {
            "word": "school",
            "hint": "A place where students study"
        },
        {
            "word": "coding",
            "hint": "Writing instructions for computers"
        },
        {
            "word": "mouse",
            "hint": "A computer pointing device"
        }
    ],

    "medium": [
        {
            "word": "computer",
            "hint": "An electronic machine used for computing"
        },
        {
            "word": "keyboard",
            "hint": "A device used for typing"
        },
        {
            "word": "developer",
            "hint": "A person who creates software"
        },
        {
            "word": "internet",
            "hint": "A global network of computers"
        },
        {
            "word": "database",
            "hint": "A structured collection of information"
        }
    ],

    "hard": [
        {
            "word": "programming",
            "hint": "The process of creating computer programs"
        },
        {
            "word": "algorithm",
            "hint": "A step-by-step method for solving a problem"
        },
        {
            "word": "cybersecurity",
            "hint": "Protection of computer systems and networks"
        },
        {
            "word": "technology",
            "hint": "Practical application of scientific knowledge"
        },
        {
            "word": "artificial",
            "hint": "Not occurring naturally"
        }
    ]
}


# ---------------------------------------------------------
# GAME SETTINGS
# ---------------------------------------------------------

difficulty_settings = {
    "easy": 6,
    "medium": 5,
    "hard": 4
}


# ---------------------------------------------------------
# GAME STATISTICS
# ---------------------------------------------------------

games_played = 0
games_won = 0
games_lost = 0
total_score = 0
high_score = 0


# ---------------------------------------------------------
# DISPLAY TITLE
# ---------------------------------------------------------

def show_title():
    print("\n" + "=" * 60)
    print("                 HANGMAN GAME ")
    print("=" * 60)
    print("             CodeAlpha - Task 1")
    print("=" * 60)


# ---------------------------------------------------------
# CHOOSE DIFFICULTY
# ---------------------------------------------------------

def choose_difficulty():

    print("\nChoose Difficulty")
    print("-" * 35)

    print("1. Easy   → 6 wrong guesses")
    print("2. Medium → 5 wrong guesses")
    print("3. Hard   → 4 wrong guesses")

    while True:

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            return "easy"

        elif choice == "2":
            return "medium"

        elif choice == "3":
            return "hard"

        else:
            print("❌ Invalid choice. Please enter 1, 2 or 3.")


# ---------------------------------------------------------
# DISPLAY WORD
# ---------------------------------------------------------

def display_word(word, guessed_letters):

    display = ""

    for letter in word:

        if letter in guessed_letters:
            display += letter.upper() + " "
        else:
            display += "_ "

    return display


# ---------------------------------------------------------
# CHECK IF WORD IS COMPLETE
# ---------------------------------------------------------

def word_is_complete(word, guessed_letters):

    for letter in word:

        if letter not in guessed_letters:
            return False

    return True


# ---------------------------------------------------------
# SHOW STATISTICS
# ---------------------------------------------------------

def show_statistics():

    print("\n" + "=" * 50)
    print("                 STATISTICS")
    print("=" * 50)

    print("Games Played :", games_played)
    print("Games Won    :", games_won)
    print("Games Lost   :", games_lost)
    print("Total Score  :", total_score)
    print("High Score   :", high_score)

    if games_played > 0:

        win_rate = (games_won / games_played) * 100

        print(f"Win Rate     : {win_rate:.1f}%")

    else:

        print("Win Rate     : 0%")

    print("=" * 50)


# ---------------------------------------------------------
# SAVE HIGH SCORE
# ---------------------------------------------------------

def save_high_score():

    with open("highscore.txt", "w") as file:

        file.write(str(high_score))


# ---------------------------------------------------------
# LOAD HIGH SCORE
# ---------------------------------------------------------

def load_high_score():

    try:

        with open("highscore.txt", "r") as file:

            return int(file.read())

    except (FileNotFoundError, ValueError):

        return 0


# ---------------------------------------------------------
# CALCULATE SCORE
# ---------------------------------------------------------

def calculate_score(word, difficulty, wrong_guesses, hints_used):

    # Basic score based on word length
    score = len(word) * 10

    # Difficulty bonus
    if difficulty == "medium":

        score += 20

    elif difficulty == "hard":

        score += 40

    # Penalty for wrong guesses
    score -= wrong_guesses * 5

    # Penalty for hints
    score -= hints_used * 10

    # Score should never be negative
    if score < 0:

        score = 0

    return score


# ---------------------------------------------------------
# USE HINT
# ---------------------------------------------------------

def use_hint(word_data, guessed_letters):

    word = word_data["word"]
    clue = word_data["hint"]

    # Find letters which are still hidden
    hidden_letters = []

    for letter in word:

        if letter not in guessed_letters:

            if letter not in hidden_letters:

                hidden_letters.append(letter)

    # If no hidden letters remain
    if len(hidden_letters) == 0:

        print("\n⚠️ There are no hidden letters left.")

        return False

    # Show clue
    print("\n" + "-" * 50)
    print("💡 HINT")
    print("-" * 50)

    print("Clue:", clue)

    # Randomly reveal one hidden letter
    revealed_letter = random.choice(hidden_letters)

    guessed_letters.append(revealed_letter)

    print(
        "🔤 Revealed letter:",
        revealed_letter.upper()
    )

    print("-" * 50)

    return True


# ---------------------------------------------------------
# PLAY ONE GAME
# ---------------------------------------------------------

def play_game():

    global games_played
    global games_won
    global games_lost
    global total_score
    global high_score

    # Select difficulty
    difficulty = choose_difficulty()

    # Select random word
    word_data = random.choice(words[difficulty])

    word = word_data["word"]

    # Maximum wrong guesses
    max_wrong_guesses = difficulty_settings[difficulty]

    # Game variables
    guessed_letters = []

    wrong_guesses = 0

    hints_used = 0

    games_played += 1

    # Game start
    print("\n" + "=" * 60)
    print("                GAME STARTED")
    print("=" * 60)

    print("Difficulty:", difficulty.upper())
    print("Wrong guesses allowed:", max_wrong_guesses)

    # -----------------------------------------------------
    # GAME LOOP
    # -----------------------------------------------------

    while wrong_guesses < max_wrong_guesses:

        print("\n")
        print("Word :", display_word(word, guessed_letters))

        if guessed_letters:

            letters = ", ".join(
                letter.upper()
                for letter in guessed_letters
            )

            print("Guessed letters:", letters)

        else:

            print("Guessed letters: None")

        print(
            "Wrong guesses:",
            wrong_guesses,
            "/",
            max_wrong_guesses
        )

        print("\nOptions")
        print("-" * 30)

        print("1. Guess a letter")
        print("2. Use hint")
        print("3. Quit game")

        choice = input("\nChoose an option: ").strip()

        # -------------------------------------------------
        # OPTION 1 - GUESS LETTER
        # -------------------------------------------------

        if choice == "1":

            guess = input(
                "\nEnter a letter: "
            ).lower().strip()

            # Validate input
            if len(guess) != 1 or not guess.isalpha():

                print(
                    "❌ Please enter exactly ONE alphabet letter."
                )

                continue

            # Check duplicate guess
            if guess in guessed_letters:

                print(
                    "⚠️ You already guessed that letter."
                )

                continue

            # Add guess
            guessed_letters.append(guess)

            # Correct guess
            if guess in word:

                print(
                    "✅ Correct! The letter is in the word."
                )

            # Wrong guess
            else:

                wrong_guesses += 1

                print(
                    "❌ Wrong guess!"
                )

                print(
                    "You have",
                    max_wrong_guesses - wrong_guesses,
                    "guesses left."
                )

        # -------------------------------------------------
        # OPTION 2 - HINT
        # -------------------------------------------------

        elif choice == "2":

            # Only one hint per game
            if hints_used >= 1:

                print(
                    "\n⚠️ You can use only ONE hint per game."
                )

                continue

            # Use hint
            hint_success = use_hint(
                word_data,
                guessed_letters
            )

            if hint_success:

                hints_used += 1

        # -------------------------------------------------
        # OPTION 3 - QUIT
        # -------------------------------------------------

        elif choice == "3":

            print("\nYou quit the game.")

            print(
                "The correct word was:",
                word.upper()
            )

            games_lost += 1

            return

        # -------------------------------------------------
        # INVALID OPTION
        # -------------------------------------------------

        else:

            print(
                "❌ Invalid option. Choose 1, 2 or 3."
            )

            continue

        # -------------------------------------------------
        # CHECK WIN
        # -------------------------------------------------

        if word_is_complete(
            word,
            guessed_letters
        ):

            score = calculate_score(
                word,
                difficulty,
                wrong_guesses,
                hints_used
            )

            games_won += 1

            total_score += score

            print("\n" + "=" * 60)
            print("             🎉 YOU WON! 🎉")
            print("=" * 60)

            print(
                "The word was:",
                word.upper()
            )

            print(
                "Your score:",
                score
            )

            # Check high score
            if score > high_score:

                high_score = score

                save_high_score()

                print(
                    "🏆 NEW HIGH SCORE!"
                )

            else:

                print(
                    "Current high score:",
                    high_score
                )

            return

    # -----------------------------------------------------
    # GAME OVER
    # -----------------------------------------------------

    games_lost += 1

    print("\n" + "=" * 60)
    print("               💀 GAME OVER")
    print("=" * 60)

    print(
        "The correct word was:",
        word.upper()
    )


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():

    global high_score

    # Load saved high score
    high_score = load_high_score()

    while True:

        show_title()

        print("\nMAIN MENU")
        print("-" * 30)

        print("1. Start Game")
        print("2. Statistics")
        print("3. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # Start game
        if choice == "1":

            play_game()

        # Statistics
        elif choice == "2":

            show_statistics()

        # Exit
        elif choice == "3":

            print("\n" + "=" * 50)
            print("Thanks for playing Hangman ! 👋")
            print("=" * 50)

            break

        # Invalid choice
        else:

            print(
                "\n❌ Invalid choice. Please try again."
            )


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":

    main()