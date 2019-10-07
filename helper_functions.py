# -*- coding: UTF-8 -*-

# Author: Raymond Andrade
# Date:   October 2019

# Description: Helper classes for blackjack.py program

import sys
import random


class Cards:
	def __init__(self, card_game):
		self.card_game = card_game
		self.numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
		self.suits = ["♣", "♠", "♥", "♦"]

	def deal_random_card(self):		# Select random number and suit to simulate dealing a card
		rand_card = self.numbers[random.randint(0, len(self.numbers)-1 )]
		rand_suit = self.suits[random.randint(0, len(self.suits)-1 )]

		card = str(rand_card) + rand_suit

		return card

	def print_card(self, card):		# Print card to terminal screen
		suite_row = " |" + card + " |"

		if len(card) == 3:
			suite_row = " |" + card + "|"

		print(" -----")
		print(suite_row)
		print(" |   |")
		print(" -----")

	def refresh_screen(self, cards): # Clear terminal screen and repopulate cards
		print(chr(27) + "[2J")

		for card in cards:
			self.print_card(card)


class Player:
	def __init__(self, name, card_game):
		self.name = name
		self.card_game = card_game
		self.cards = []

	def add_card(self, card):
		self.cards.append(card)

	def check_cards_value(self):     # Method to add the values of the card the player has
		possible_player_values = [0] # To accompany the fact that an Ace can be a 1 or 11

		for card in self.cards:
			card_value = card[0] # Only takes the first digit of the card, not the suit, since 10 has two digits, 10 is added if 1 is detected

			if card_value == "J" or card_value == "Q" or card_value == "K" or card_value == "1":
				possible_player_values = [x+10 for x in possible_player_values]

			elif card_value == "A":
				possible_player_values.append(possible_player_values[-1])
				possible_player_values = [x+1 for x in possible_player_values]
				possible_player_values[-1] += 10 # Add Last Entry by 10 since 1 was added to all value already

			else:
				# print(card_value)
				possible_player_values = [x+int(card_value) for x in possible_player_values]


		for value_index in sorted(range(len(possible_player_values)), reverse=True):
			value = possible_player_values[value_index]

			if value > 21:
				del possible_player_values[value_index]


		return possible_player_values

	def prompt(self, prompt_text):    # Prompts the user, checks for python version to use proper input function
		if sys.version_info[0] == 2:
			return raw_input(prompt_text)
		elif sys.version_info[0] == 3:
			return input(prompt_text)
		else:
			sys.exit("Invalid Python Version Detected")

