"""Generator Exercises."""


def is_prime(number):
	"""Return True if candidate number is prime."""

	return all(number % factors != 0 for factors in range(2, number))

def all_together(*iterables):
	"""String together all items from the given iterables."""

	return (element for iterable in iterables for element in iterable)

def interleave(iterable1, iterable2):
	"""Return iterable of one item at a time from each list."""

	return (element for zipped_element in zip(iterable1, iterable2) for element in zipped_element)

def translate(sentence):
	"""Return a transliterated version of the given sentence."""

	words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
	return ' '.join(words[word] for word in sentence.split() if word in words)

def parse_ranges(ranges_string):
	"""Return a list of numbers corresponding to number ranges in a string"""

	return (number_ranges # Flatten the list of list ranges.
			for range_lists in ( # Save a list of lists containing all numbers in those ranges.
				range(int(range_list[0]), int(range_list[1]) + 1) 
				for range_list in ( # Save a list of tuples containing all given ranges.
					range_list
					for ranges in ranges_string.split(',')
					for range_list in [tuple(ranges.split('-'))]
				)
			)
			for number_ranges in range_lists)

def first_prime_over(number):
	"""Return the first prime number over a given number."""

	while True:
		if is_prime(number):
			return number
		else:
			number += 1

def is_anagram(string1, string2):
	"""Return True if the given words are anagrams."""

	punctuation_list = [',', '.', ' ', "'", '"', ':', ';']

	string1_list = sorted([element1.lower() for element1 in string1 if element1 not in punctuation_list])
	string2_list = sorted([element2.lower() for element2 in string2 if element2 not in punctuation_list])

	return all(zipped[0] == zipped[1]
			   if len(string1_list) == len(string2_list) else False
			   for zipped in zip(string1_list, string2_list))
