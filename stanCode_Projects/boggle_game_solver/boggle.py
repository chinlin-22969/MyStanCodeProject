"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	This program will present the word game "boggle", which helps find words which contains four or more letters
	on the 4*4 chart of letters.
	"""
	# Get inputs from user and make it into a dictionary. ([column, row]: letter, [1, 3]:'a')
	input_d = get_input_letters()

	# Read through the file and make usable words into a dictionary. (1st letter: [words,...], 'a':['apple', 'ape'...])
	word_d = read_dictionary(input_d)

	# Loop through each input letter and make an answer list
	ans_lst = []
	for i in range(4):
		for j in range(4):
			target_letter = input_d[(j, i)]
			boggle(target_letter, [(j, i)], j, i, ans_lst, word_d, input_d)
	print(f'There are {len(ans_lst)} words in total.')


def get_input_letters():
	"""
	This function ask the user to input letters in the form of boggle game.

	:return input_d:(dict) A dictionary contains input letters. ([column, row]: letter, [1, 3]:'a')
	"""
	input_d = {}
	# Ask the user to input four rows of letter
	for i in range(4):
		s = input(f'{i+1} row of letters: ')
		# Program stops if illegal input happens
		if len(s) != 7 or s[1] + s[3] + s[5] != '   ':
			print('Illegal input')
			exit()

		# For loop through substring make it into a dictionary (key: value --> [column, row]: letter)
		sub_str = ''.join(s.split())
		for j in range(4):
			input_d[j, i] = sub_str[j]
		# Turn all the substring into a string(ex: 'fifcemukyukaowcr')
	return input_d


def read_dictionary(d):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and find out the words which starts with the letter in s
	and make it into a dictionary.(key: value --> letter in s: words start with the letter in s)

	:param d:(dict) A dictionary contains input letters ([column, row]: letter, [1, 3]:'a')
	:return word_dict:(dict) A dictionary contains words which starts with letters in s. (ex: 'a':['apple', 'ape'...])
	"""
	word_dict = {}
	with open(FILE) as f:
		for line in f:
			word = line.strip()  # get rid of space & \n
			if word[0] in d.values():
				if word[0] in word_dict:
					word_dict[word[0]].append(word)
				else:
					word_dict[word[0]] = [word]
	return word_dict


def has_prefix(sub_s, word_dict):
	"""
	This function check if there is any words in word_dict with prefix 'sub_s'.

	:param sub_s:(str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param word_dict:(dict) A dictionary contains all the words which starts with the letter in user inputs.
	ex:{'a':['apple',..], 'b':['booth'...].....}

	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in word_dict[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


def boggle(cur_str, cur_lst, cur_x, cur_y, ans_lst, word_d, input_d):
	"""
	This function concatenate the surrounding letters to cur_str and check if it fix has_prefix.
	Will print every answer and store it in the ans_lst.

	:param cur_str:(str) current string starts with an input letter
	:param cur_lst:(lst)A list contains the x, y location of the input letters
	:param cur_x:(int) current x location(column)
	:param cur_y:(int) current y location(row)

	:param ans_lst:(lst) A list contains the answer string
	:param input_d:(dict) A dictionary key:value -->  location: input letter  ex:{(0, 0):'f', (1, 0):'y'.....}
	:param word_d:(dict) A dictionary contains all the words which starts with the letter in user inputs


	This function do not return.
	"""
	# Base-case
	if len(cur_str) >= 4:   # From the game rule, the word needs to contain four or more letters
		if cur_str not in ans_lst:
			if cur_str in word_d[cur_str[0]]:
				print(f'Found: "{cur_str}"')
				ans_lst.append(cur_str)

	# Find the surrounding letters, and check if it fits has_prefix
	for y in range(-1, 2):
		for x in range(-1, 2):
			# Choose
			if (cur_x+x, cur_y+y) not in cur_lst:
				if 0 <= cur_x+x < 4 and 0 <= cur_y+y < 4:
					cur_x += x
					cur_y += y
					cur_str += input_d[(cur_x, cur_y)]
					cur_lst.append((cur_x, cur_y))

					# Explore
					if has_prefix(cur_str, word_d):
						boggle(cur_str, cur_lst, cur_x, cur_y, ans_lst, word_d, input_d)

					# Un-choose
					cur_x -= x
					cur_y -= y
					cur_str = cur_str[:-1]
					cur_lst.pop()


if __name__ == '__main__':
	main()
