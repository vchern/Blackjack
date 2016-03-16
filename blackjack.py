from random import randint

freshDeck = []
deck = []
burnedDeck = []
number = ["A", "2", "3", "4", "5", "6", "7", "8", "9" , "10", "J", "Q", "K"]
suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
global card1
global card2

def shuffle():
	for i in range (0, 52):
		deck.append(i)

def deal():
	card1 = deck[randint(0, len(deck)-1)]
	if card1 < 0:
		card1 = dealIndividual(card1)
	deck[card1] = -1
	burnedDeck.append(card1)
	card2 = deck[randint(0, len(deck)-1)]
	if card2 < 0:
		card2 = dealIndividual(card2)
	deck[card2] = -1
	burnedDeck.append(card2)
	card1Number = number[card1//4]
	card1Suit = suit[card1 % 4]
	card2Number = number[card2//4]
	card2Suit = suit[card2 % 4]
	print("You are dealt the {} of {} and the {} of {}".format(card1Number, card1Suit, card2Number, card2Suit))
	#return (card1Number, card1Suit, card2Number, card2Suit)

def dealIndividual(card):
	while card < 0:
		card = deck[randint(0, len(deck)-1)]
	return card

def main():
	shuffle()
	deal()

if __name__ == "__main__":
	main()
