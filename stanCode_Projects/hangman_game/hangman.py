"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    """
    current_word = ''
    answer = random_word()
    wrong_guess = N_TURNS
    for i in range(len(answer)):
        current_word += '_'
    print('The word looks like '+str(current_word))
    print('You have '+str(N_TURNS) + ' wrong guesses left.')
    while True:
        ch = input('Your guess: ')
        # check if the format is legal
        if ch.isalpha() is False or len(ch) > 1:
            print('Illegal format.')
        else:
            ch = ch.upper()
        # check if it’s the right guess
            if answer.find(ch) != -1:
                new_word = ''
                for i in range(len(answer)):
                    if answer[i] == ch:
                        new_word += ch
                    else:
                        new_word += current_word[i]
                print('You are correct!')
                draw_hangman(wrong_guess)
                print('The word looks like ' + str(new_word))
                print('***' * 20)
                current_word = new_word
            else:
                print('There is no ' + str(ch) + ' in the word.')
                print('The word looks like ' + str(current_word))
                wrong_guess -= 1
                draw_hangman(wrong_guess)
                print('You have '+str(wrong_guess) + ' wrong guesses left.')
                print('***'*20)
        if wrong_guess < 1:
            print('You are completely hung: (')
            draw_hangman(wrong_guess)
            print('The word was: '+str(answer))
            break
        if current_word.find('_') == -1:
            print('You are correct!')
            print('You win!')
            print('The word was: '+str(answer))
            print('_' * 13, '\n|/', ' ' * 8, '|',
                  '\n|',
                  '\n|',
                  '\n|', ' ' * 13, '(^ ^)',
                  '\n|', ' ' * 14, '\\|/',
                  '\n|', ' ' * 15, '|',
                  '\n---', ' ' * 12, '/ \\')
            break


def draw_hangman(n):
    if n == 7:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|' * 5, '\n---')
    if n == 6:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|', ' ' * 8, '(   )',
              '\n|' * 4, '\n---')
    if n == 5:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|', ' ' * 8, '(   )',
              '\n|', ' ' * 8, ' |',
              '\n|', ' ' * 9, '|',
              '\n|' * 2, '\n---')
    if n == 4:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|', ' ' * 8, '(   )',
              '\n|', ' ' * 8, '/|',
              '\n|', ' ' * 9, '|',
              '\n|' * 2, '\n---')
    if n == 3:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|', ' ' * 8, '(   )',
              '\n|', ' ' * 8, '/|\\',
              '\n|', ' ' * 9, '|',
              '\n|' * 2, '\n---')
    if n == 2:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|', ' ' * 8, '(   )',
              '\n|', ' ' * 8, '/|\\',
              '\n|', ' ' * 9, '|',
              '\n|', ' ' * 8, '/ ',
              '\n|' * 1, '\n---')
    if n == 1:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|', ' ' * 8, '(   )',
              '\n|', ' ' * 8, '/|\\',
              '\n|', ' ' * 9, '|',
              '\n|', ' ' * 8, '/ \\',
              '\n|' * 1, '\n---')
    if n == 0:
        print('_' * 13, '\n|/', ' ' * 8, '|',
              '\n|', ' ' * 8, '(x x)',
              '\n|', ' ' * 8, '/|\\',
              '\n|', ' ' * 9, '|',
              '\n|', ' ' * 8, '/ \\',
              '\n|' * 1, '\n---')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
