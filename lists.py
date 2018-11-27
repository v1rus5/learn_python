"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    return [name for name in names if name[0].lower() in vowel_list]

def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    return [number ** power for power, number in enumerate(numbers)] 

def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [elements for row in matrix for elements in row]

def reverse_difference(numbers):
    """Return list subtracted from the reverse of itself."""
    return [elements - reverse for elements, reverse in zip(numbers, numbers[::-1])]

def matrix_add(mat1, mat2):
    """Add corresponding numbers in given 2-D matrices."""
    return [[elem1 + elem2 for elem1, elem2 in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]

def transpose(matrix):
    """Return a transposed version of given list of lists."""
    #if not matrix:
    #    return []

    #return [[row[i] for row in matrix] for i in range(max(len(row) for row in matrix))]
    return [list(row) for row in zip(*matrix)]

def get_factors(number):
    """Return a list of all factors of the given number."""
    return [fact for fact in range(1, number+1) if number % fact == 0]

def triples(number):
    """Return list of Pythagorean triples less than input num."""
    return [(a, b, c) for a in range(1, number+1) for b in range(a, number+1) for c in range(b, number+1) if a**2 + b**2 == c**2 and a < number and b < number and c < number]
