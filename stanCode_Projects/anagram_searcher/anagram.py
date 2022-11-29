"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""


# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: Find all the anagrams of the input word!
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    s = input('Find anagrams for: ')
    find_anagrams(s)


def read_dictionary(s):
    """
    :param s:(str) the input word from user
    :return words_lst:(list) A list of words from the FILE having the same length as s
    and containing all the characters of s
    """
    words_lst = []
    with open(FILE) as f:
        for line in f:
            word = line.strip()
            if len(word) == len(s):  # find out words which it's length equal to s's
                if sorted(word) == sorted(s):  # find out words which contains all the character in s
                    words_lst.append(line.strip())
    return words_lst


def has_prefix_helper(sub_s, words_lst):
    """
    :param sub_s:(str) part of the input words
    :param words_lst:(list) A list of given words
    :return Boolean
    """
    for word in words_lst:
        if word.startswith(sub_s):
            return True
    return False


def find_anagrams(s):
    """
    :param s:(str) The input word from user
    This function returns nothing.
    """
    s_lst = []
    for i in range(len(s)):
        s_lst.append((i, s[i]))
    ans_lst = find_anagrams_helper(s, s_lst, [], '', [], read_dictionary(s), len(s))
    print(f'{len(ans_lst)} anagrams: {ans_lst}')


def index_exist(index, cur_lst):
    """
    :param index: (int) the index of the character
    :param cur_lst: (list) A list of tuples containing index and character
    :return Boolean
    """
    for t in cur_lst:
        if index == t[0]:
            return True
    return False


def find_anagrams_helper(s, s_lst, cur_lst, cur_str, ans_lst, words_lst, ans_len):
    """
    :param s: (str)The input word from user /ex: arm
    :param s_lst: (list) A list of tuples containing index and character of s /ex:[(1,'a'), (2,'r'), (3,'m')]
    :param cur_lst: (list) A list holding current tuples containing index and character/ ex:[(3,'m'), (1,'a')]
    :param cur_str: (str) holding the current string/ ex:'ma'
    :param ans_lst: (list) A list holding anagrams of s
    :param words_lst: (list) A list of words having the same length as s from the FILE
    :param ans_len: (int) The length of s

    :return ans_lst: (list) A list holding anagrams of s
    """
    if cur_str in read_dictionary(s):
        if cur_str not in ans_lst:
            print('Searching...')
            print(f'Found: {cur_str}')
            ans_lst.append(cur_str)
    else:
        for t in s_lst:
            if not index_exist(t[0], cur_lst):
                # Choose
                cur_lst.append(t)
                cur_str += t[1]
                # Explore
                if has_prefix_helper(cur_str, words_lst):
                    find_anagrams_helper(s, s_lst, cur_lst, cur_str, ans_lst, words_lst, ans_len)
                # Un-choose
                cur_lst.pop()
                cur_str = cur_str[:len(cur_str) - 1]
    return ans_lst


if __name__ == '__main__':
    main()
