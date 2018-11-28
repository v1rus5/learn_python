"""More comprehension exercises"""


def flip_dict(given_dict):
	"""Return a new dictionary that maps the original values to the keys."""

	return {key:value for value, key in given_dict.items()}

def get_ascii_codes(string_list):
	"""Return a dictionary mapping the strings to ASCII codes."""

	return {word:[ord(chr) for chr in word] for word in string_list}

def dict_from_truple(tuple_list):
	"""Turn three-item tuples into a dictionary of two-valued tuples."""

	return {tuple_element[0]:tuple_element[1:] for tuple_element in tuple_list} 

def dict_from_tuple(tuple_list):
	"""Turn multi-item tuples into a dictionary of two-valued tuples."""

	return {tuple_element[0]:tuple_element[1:] for tuple_element in tuple_list}

def get_all_factors(set_of_numbers):
	"""Return a dictionary mapping numbers to their factors."""

	return {number:[factor for factor in range(1, number+1) if number % factor == 0] for number in set_of_numbers}
