"""Advanced exercises"""
from collections import namedtuple
import csv

import random


def matrix_from_string(string):
	"""Convert rows of numbers to list of lists."""

	return [[int(number) for number in row.split(' ')] for row in string.split('\n')]

def parse_csv(file_obj):
	"""Return namedtuple list representing data from given file object."""
	#csv_reader = csv.reader(file_obj)
	#Row = namedtuple('Row', next(csv_reader))

	with open(file_obj.name, mode=file_obj.mode) as csv_file:
		csv_rows = csv.reader(csv_file)

		csv_elements = [tuple(row) for row in csv_rows]
		csv_header = csv_elements.pop(0)
		named_tuple = namedtuple('X', csv_header)
		return [named_tuple(*element) for element in csv_elements]
		

def get_cards():
	"""Create a list of namedtuples representing a deck of playing cards."""

	Card = namedtuple('Card', ['rank', 'suit'])
	ranks = list('A') + [str(n) for n in range(2, 11)] + list('JQK')
	suits = ['spades', 'hearts', 'diamonds', 'clubs']
	deck = [Card(rank, suit) for suit in suits for rank in ranks]
	return deck


def shuffle_cards(deck):
	"""Shuffles a list in-place"""
	random.shuffle(deck)


def deal_cards(deck, count=5):
	"""Remove the given number of cards from the deck and returns them"""

	return [deck.pop() for elem in range(len(deck)) if elem < count]
