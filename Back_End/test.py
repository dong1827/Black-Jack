from Deck import Deck
from Player import Player

deck = Deck()

deck.shuffle()
p = Player(100)

print(p.add_cards((1, "Diamond")))
print(p.peak_deck())
print(p.add_cards((13, "Spades")))
print(p.peak_value())
print(p.add_cards((5, "Diamond")))
print(p.peak_value())
