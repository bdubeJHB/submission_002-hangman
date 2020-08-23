import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
        return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ").strip()
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


def random_fill_word(word):
    given = list(word)
    count = 0
    index = random.randint(0, len(given) - 1)

    while count < len(given):
        if count != index:
            given[count] = '_'
        count += 1
    return ''.join(given)



def is_missing_char(original_word, answer_word, char):
    if char in original_word:
        index = 0
        while index < len(original_word):
            if original_word[index] == char and answer_word[index] == '_':
                return True
            index += 1
    return False


def fill_in_char(original_word, answer_word, char):
    word = list(answer_word)
    index = 0

    while index < len(original_word):
        if original_word[index] == char and answer_word[index] == '_':
            word[index] = char
        index += 1

    return ''.join(word)


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    if number_guesses:
        print('Wrong! Number of guesses left: ' + str(number_guesses))
    else:
        print("Sorry, you are out of guesses. The word was " + answer)
    draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 5:
        print("/----\n|\n|\n|\n|")
    elif number_guesses == 4:
        print("/----\n|   0\n|\n|\n|\n")
    elif number_guesses == 3:
        print("/----\n|   0\n|  /|\\\n|\n|")
    elif number_guesses == 2:
        print("/----\n|   0\n|  /|\\\n|   |\n|")
    else:
        print("/----\n|   0\n|  /|\\\n|   |\n|  / \\")

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    #print(answer + " && " + word)
    lives = 5

    while lives:
        print("Guess the word: " + answer)
        if '_' not in answer:
            break
        guess = get_user_input().strip().lower()
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        elif guess == "quit" or guess == "exit":
            print("Bye!")
            break
        else:
            do_wrong_answer(answer, lives)
            lives -= 1


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

