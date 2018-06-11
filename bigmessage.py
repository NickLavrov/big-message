#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from alphabet import alphabet, height

def convert_phrase(phrase, background, foreground, border):
	msg = ''
	phrase = phrase.split(' ')

	for word_index, word in enumerate(phrase):
		output = [[] for i in range(height)]

		# fill in each character
		for i, c in enumerate(word):
			width = len(alphabet[c])//height
			for row in range(len(output)):
				output[row].extend(alphabet[c][row*width:(row+1)*width])
				# insert char spacing
				if i != len(word)-1:
					output[row].append(0)

		# add border
		if border:
			for row in output:
				row.insert(0, 0)
				row.append(0)
			if word_index == 0:
				output.insert(0, [0]*(len(output[0])))
			output.append([0]*(len(output[0])))

		# convert to emoji
		for row in output:
			text = [foreground if pixel==1 else background for pixel in row]
			msg += ''.join(text) + '\n'

		# add empty row or border between words
		if word_index != len(phrase)-1 and not border:
			msg += '\n'

	return msg

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Turn a phrase into emoji pixel font.',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('phrase')

	parser.add_argument('-b', '--background', action='store',
		default='◻️', help='Emoji to use for background')

	parser.add_argument('-f', '--foreground', action='store',
		default='◼️', help='Emoji to use for the foreground font')

	parser.add_argument('-B', '--border', action='store_true',
		default=False, help='Surround output with a border')

	parser.add_argument('-v', '--version', action='version',
		version='%(prog)s 1.0')

	args = parser.parse_args()

	print(convert_phrase(args.phrase, args.background, args.foreground, args.border))
