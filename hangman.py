import random

MAX_TRIES = 7
old_letters_guessed =[]

with open("hangman_ascii_art.txt", "r", encoding="utf-8") as hangman_ascii_art:
    HANGMAN_ASCII_ART = hangman_ascii_art.read()

with open("fireworks_ascii_art.txt", "r", encoding="utf-8") as fireworks_ascii_art:
    FIREWORKS = fireworks_ascii_art.read()

with open("won_ascii_art.txt", "r", encoding="utf-8") as won_ascii_art:
    WON = won_ascii_art.read()

with open("game_over_ascii_art.txt", "r", encoding="utf-8") as game_over_ascii_art:
    GAME_OVER = game_over_ascii_art.read()

with open("hangman_fails.txt", "r", encoding="utf-8") as fails_ascii_art:
    HANGMAN_PHOTOS = fails_ascii_art.read().split("&")


def check_valid_input(letter_guessed, old_letters_guessed):
    if (len(letter_guessed) > 1 or not letter_guessed.isalpha()
            or letter_guessed.lower() in old_letters_guessed
            or letter_guessed.upper() in old_letters_guessed):
        return False
    elif (len(letter_guessed) == 1 and letter_guessed.isalpha()
          and letter_guessed.lower() not in old_letters_guessed
          and letter_guessed.upper() not in old_letters_guessed):
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    return False


def check_letter(letter):
    if len(letter) > 1 and letter.isalpha():
        print('E1 --> the input too long')
    elif not letter.isalpha() and len(letter) < 2:
        print('E2 --> the input is not a letter')
    elif not letter.isalpha() and len(letter) > 1:
        print('E3 --> the input is not a letter and too long')
    elif not try_update_letter_guessed(letter, old_letters_guessed):
        print("You already guessed that letter")


def show_hidden_word(secret_word, old_letters_guessed):
    hidden_word = ''
    for letter in secret_word.lower():
        if letter in old_letters_guessed:
            hidden_word += letter + ' '
        elif letter == ' ':
            hidden_word += '  '
        else:
            hidden_word += '_ '
    return hidden_word


def check_win(secret_word, old_letters_guessed):
    list_secret_word = list(secret_word.lower())
    for secret_letter in list_secret_word:
        if secret_letter not in old_letters_guessed:
            return False
    return True


def choose_word(file_path):
    f = open(file_path, 'r')
    file = f.read().split('\n')
    words_list = []
    index = random.randint(0, len(file) - 1)
    for word in file:
        if word not in words_list:
            words_list.append(word)
    f.close()
    return file[(len(file)+1)%index]


def letter_in_secret_word(letter, secret_word,old_letters_guessed):
    if letter not in secret_word and letter not in old_letters_guessed and len(letter) < 2 and letter.isalpha():
        return True
    return False

def choose_subject(chooses_num):
    if chooses_num == '1':
        file_name = "hangman_country_names.txt"
    elif chooses_num == '2':
        file_name = "hangman_animals_names.txt"
    elif chooses_num == '3':
        file_name = "hangman_jobs_names.txt"
    elif chooses_num == '4':
        file_name = "hangman_fruits_and_vegetables_names.txt"
    else:
        print("Invalid input")
        main()
    return file_name

def print_game(q_num, secret_word='', fails=0, old_letters_guessed=[]):
    if q_num == 0:
        print(HANGMAN_PHOTOS[fails])
        print(show_hidden_word(secret_word, old_letters_guessed))
        print("The letters you have guessed are: ", old_letters_guessed)
        letter = input("Guess a letter: ")
        return letter
    elif q_num == -1:
        print(HANGMAN_PHOTOS[fails])
        print(GAME_OVER)
        print('The secret word was: ', secret_word)
    elif q_num == 1:
        print(FIREWORKS)
        print(WON)
        print('You right the secret word was: ', secret_word)

def main():
    print(HANGMAN_ASCII_ART)
    chooses_num = input("select one of the subject (inset chooses number):"+
                        "\n"+"(1)country, (2)animals, (3)jobs, (4)fruits and vegetables ")
    file_name = choose_subject(chooses_num)
    secret_word = choose_word(file_name)
    fails = 0
    while(fails < 7):
        letter = print_game(0, secret_word, fails ,old_letters_guessed)
        if letter_in_secret_word(letter, secret_word,old_letters_guessed):
            fails += 1
            if fails == 7:
                print_game(-1, secret_word, fails)
        check_letter(letter)
        if check_win(secret_word, old_letters_guessed):
            print_game(1,secret_word)
            break

if __name__ == "__main__":
    main()