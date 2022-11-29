"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: This program will present the game "boggle".
	"""
	start = time.time()
	####################
	ch_dict = {}
	s_str = ''  # fifcemukyukaowcr
	# Ask the user to input four rows of letter
	for i in range(4):
		s = input(f'{i+1} row of letters: ')
		# Program stops if illegal input happens
		if len(s) != 7 or s[1] + s[3] + s[5] != '   ':
			print('Illegal input')
			exit()

	# Turn all the input into a string
		sub_str = ''.join(s.split())
	# Turn all the input into a dictionary (key: value --> column: row)
		for j in range(4):
			ch_dict[j, i] = sub_str[j]
		s_str += sub_str

	# Word_dict contains all the words start with letters from s_str (key: value --> 1st letter: words)
	word_dict = read_dictionary(s_str)

	# Check out the answer of each input letter one by one
	ans_lst = []
	for i in range(4):
		for j in range(4):
			boggle(word_dict, [(j, i)], ch_dict, ch_dict[(j, i)], j, i, ans_lst)
	print(f'There are {len(ans_lst)} words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(s):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and find out the words which starts with the letter in s
	and make it into a dictionary.(key: value --> letter in s: words start with the letter in s)

	:param s: A string contains the input letters
	:return word_dict: A dictionary contains words which starts with character in s. {'a':['apple',..],'b':['booth'..].}
	"""
	word_dict = {}
	with open(FILE) as f:
		for line in f:
			word = line.strip()
			if word[0] in s:
				if word[0] in word_dict:
					word_dict[word[0]].append(word)
				else:
					word_dict[word[0]] = [word]
	return word_dict


def has_prefix(sub_s, word_dict):
	"""
	This function check if there is any words in word_dict with prefix 'sub_s'.

	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param word_dict: A dictionary contains all the words which starts with the letter in user inputs.
	ex:{'a':['apple',..], 'b':['booth'...].....}

	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_dict[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


def boggle(word_dict, index_lst, ch_dict, cur_str, cur_x, cur_y, ans_lst):
	"""
	This function concatenate the surrounding letters to cur_str and check if it fix has_prefix.
	Will print every words that fix the game 'boggle' and store the words in the ans_lst.

	:param word_dict: A dictionary contains all the words which starts with the letter in user inputs
	:param index_lst: A list contains the x, y location of the input letters
	:param ch_dict: A dictionary key:value -->  location: input letter  ex:{(0, 0):'f', (1, 0):'y'.....}
	:param cur_str: current string starts with an input letter
	:param cur_x: current x location(column)
	:param cur_y: current y location(row)
	:param ans_lst: A list contains the answer string

	This function do not return.
	"""
	# Base-case
	if len(cur_str) >= 4:
		if cur_str not in ans_lst:
			if cur_str in word_dict[cur_str[0]]:
				print(f'Found: "{cur_str}"')
				ans_lst.append(cur_str)

	# Find the surrounding letters, and check if it fits has_prefix
	for y in range(-1, 2):
		for x in range(-1, 2):
			# Choose
			if (cur_x+x, cur_y+y) not in index_lst:
				if 0 <= cur_x+x < 4 and 0 <= cur_y+y < 4:
					cur_x += x
					cur_y += y
					cur_str += ch_dict[(cur_x, cur_y)]
					index_lst.append((cur_x, cur_y))
					# Explore
					if has_prefix(cur_str, word_dict):
						boggle(word_dict, index_lst, ch_dict, cur_str, cur_x, cur_y, ans_lst)
					# Un-choose
					cur_str = cur_str[:-1]
					index_lst.pop()
					cur_x -= x
					cur_y -= y


if __name__ == '__main__':
	main()
