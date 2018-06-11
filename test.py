import unittest
from bigmessage import convert_phrase

import unittest

class BigMessageTestCase(unittest.TestCase):
	def test_one_character(self):
		output = convert_phrase('H', '0', '1', False)
		expected = '''1001
1001
1111
1001
1001
'''
		self.assertEqual(output, expected)

	def test_one_word(self):
		output = convert_phrase('HI', '0', '1', False)
		expected = '''10010111
10010010
11110010
10010010
10010111
'''
		self.assertEqual(output, expected)

	def test_two_words(self):
		output = convert_phrase('A B', '0', '1', False)
		expected = '''0110
1001
1111
1001
1001

1110
1001
1110
1001
1110
'''
		self.assertEqual(output, expected)

	def test_one_word_border(self):
		output = convert_phrase('HI', '0', '1', True)
		expected = '''0000000000
0100101110
0100100100
0111100100
0100100100
0100101110
0000000000
'''
		self.assertEqual(output, expected)

	def test_two_words_border(self):
		output = convert_phrase('A B', '0', '1', True)
		expected = '''000000
001100
010010
011110
010010
010010
000000
011100
010010
011100
010010
011100
000000
'''
		self.assertEqual(output, expected)

if __name__ == '__main__':
	unittest.main()
