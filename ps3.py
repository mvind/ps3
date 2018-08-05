# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 10

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# (end of helper code)
# -----------------------------------

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    if word != '':
        user_word = str(word).lower()

        freq_dict = get_frequency_dict(user_word)
        score_p1 = 0
        #Get the scores for each letter
        print(freq_dict)
        for key in freq_dict:
            #print(freq_dict[key])
            score_p1+=(SCRABBLE_LETTER_VALUES[key])*int(freq_dict[key])

        #Get second compenent score
        score_p2 = 1
        if (7*len(word)-3*(n-len(word))) > 1:
            score_p2 = 7*len(word)-3*(n-len(word))

        return score_p1*score_p2
    else:
        return 0


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={'*':1}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    word = word.lower()
    dword = {}
    guess = None
    new_hand = {}
    #Get dict for word same format as hand.
    for char in word:
        dword[char] = dword.get(char, 0) +1

    #print(list(dword.keys()))
    #print(hand)
    intersection_keys = [val for val in hand.keys() if val in dword.keys()]
    unused_keys = [val for val in hand.keys() if val not in dword.keys()]
    #print(intersection_keys)
    #print(unused_keys)

    #Check if all letters in word is in hands
    if intersection_keys == list(dword.keys()):

        #Now I check if you got all the letters
        for key in intersection_keys:
            if hand[key] >= dword[key]:
                #print('check '+key)
                new_hand[key] = hand[key] - dword[key]

            else:
                #print('hand: ', hand[key], 'word: ', dword[key])
                new_hand[key] = 0

        #Add all the unused letters back to new hand
        for key in unused_keys:
            new_hand[key] = hand[key]
        #print(new_hand)
        return new_hand
    else:
        #print('not a match')

        for key in unused_keys:
            new_hand[key] = hand[key]

        for key in intersection_keys:
            new_hand[key] = hand[key]-dword[key]

        #print(new_hand)
        return new_hand

# hand = {'t': 2, 'e': 2,'s': 1,'l':1,'a':2}
# print(update_hand({'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2},'evil'))

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #Check if the word is in word list
    valid = None
    word = word.lower()

    #Replace * with vowels and check those words
    if '*' in word:
        #print('* case')
        index = word.index('*')
        temp_word = list(word)
        for i in VOWELS:
            #Insert vowel
            temp_word.pop(index)             #remove *
            temp_word.insert(index, i)       #insert vowel

            for w in word_list:
                if ''.join(temp_word) == w.lower():
                    #print('Wildcard word match found')
                    #word = ''.join(temp_word)
                    valid = True                       #Right now we just choose one if theres more than one wildcard word matching
                    break

    else:
        for w in word_list:
            if word.lower() == w.lower():
                valid = True
                break

    #Check that word is in word list, if not return false.
    if not valid:
        return False

    #Check hand has enough letters for word
    dword = get_frequency_dict(word)
    #print(dword)
    try:
        for i in word:
            if hand[i] >= dword[i]:
                #print('check')
                pass
            else:
                #print('not enough letters in hand', i)
                return False

    except KeyError:
        print('KeyError')
        return False
    return True

#print(is_valid_word('R*pture',{'r': 2, '*': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1},word_list))

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    val = list(hand.values())
    return sum(val)

def play_hand(hand, word_list):
    total_score = 0
    playing_hand = hand
    print('\n')

    while True:
        if calculate_handlen(playing_hand) == 0:
            print('\nRan out of letters. Total score: ', total_score)
            break

        print('Current hand: ')
        display_hand(playing_hand)
        ans = input('Enter word, or "!!" to indicate that you are finished: ')

        if ans == "!!":
            print('Total score: ', total_score)
            break

        #Check if the word is valid
        if is_valid_word(ans, playing_hand, word_list):
            score = get_word_score(ans, calculate_handlen(playing_hand))
            total_score += score
            print('"'+ans+'"', 'earned: ', score, '. Your total score is: ', total_score)
            #print(update_hand(hand,ans))
            playing_hand = update_hand(playing_hand, ans)

        else:
            print('"'+ans+'"', 'is not a valid word. Please choose another one.')
            #print(update_hand(hand,ans))
            playing_hand = update_hand(playing_hand, ans)

    return total_score

#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    new_hand = hand

    if letter not in list(new_hand.keys()):
        print('Letter can not be substitued because its not in your hand')
        return new_hand
    else:
        copies = new_hand[letter]
        new_hand[letter] = new_hand.get(letter, 0) - copies

        letter_choices = VOWELS + CONSONANTS+'*'

        #Remove all the letters you already have from the random choice pool
        for char in list(new_hand.keys()):
            i  = letter_choices.index(char)
            letter_choices = letter_choices[:i]+letter_choices[1+i:] #slice out char

        #Now random choose new letter and add to return_hand
        x = random.choice(letter_choices)
        new_hand[x] = new_hand.get(x, 0) + copies


        return new_hand


#substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    number_of_hands = input('Enter total number of hands: ')
    score = 0
    userHasSubstituted = False

    for i in range(int(number_of_hands)):
        print(str(i +1) + " Game")
        print('__________________________________')
        hand = deal_hand(HAND_SIZE)

        display_hand(hand)

        if userHasSubstituted == False:
            sub = input('Would like to substitue a letter in your hand (this can only be done once) y/n: ')


        if sub == 'y' and userHasSubstituted == False:
            letter = input('Input the letter which you want to substitute: ')
            #print(hand.keys())
            hand = substitute_hand(hand, letter)
            userHasSubstituted = True


        score += play_hand(hand, word_list)

    print('Game is over. Total score is: ' + str(score))

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
