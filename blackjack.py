# -*- coding: UTF-8 -*-

# Author: Raymond Andrade
# Date:   October 2019

# Description: A program to be run in terminal to play a game of blackjack

import sys
from helper_functions import Cards, Player


dealer = Cards("Blackjack")
player = Player("Jimmy", "Blackjack")

starting_card = dealer.deal_random_card()
dealer.print_card(starting_card)
player.add_card(starting_card)

action = "Start"

while action != "q":
	dealer.refresh_screen(player.cards)

	player_card_value = player.check_cards_value()
	print("Cards Value: " + str(player_card_value))


	if len(player_card_value) == 0:
		sys.exit("Busted! Please Try Again.")

	action = player.prompt("\nHit (h), Stand (s), or Quit (q): ")

	if action == "h":
		next_card = dealer.deal_random_card()
		while next_card in player.cards:   # Ensure the random card generated does not already exist
			next_card = dealer.deal_random_card()
			
		player.add_card(next_card)

	elif action == "s":
		sys.exit("Your Final Score was " + str(player.check_cards_value()[-1]) + ". Thanks For Playing!")

	elif action == "q":
		sys.exit("Thanks For Playing")

	else:
		sys.exit("An Invalid Key Was Pressed...")


