import random

class Deck:
    

    def __init__(self):
        self.card = []
        self.counter = -1
        for i in range(1, 14):
            self.card.append((i, "Hearts"))
            self.card.append((i, "Diamonds"))
            self.card.append((i, "Clubs"))
            self.card.append((i, "Spades"))

    def __init__(self, cards, counter):
        self.card = cards
        self.counter = counter

    def shuffle(self):
        self.counter = -1

        for _ in range(300, random.randint(300, 1000)):
            swap1 = random.randint(0, 51)
            swap2 = random.randint(0, 51)

            temp = self.card[swap1]
            self.card[swap1] = self.card[swap2]
            self.card[swap2] = temp

        for _ in range(0, 3):
            cut = random.randint(10, 40)
            temp_card = []
            for i in range(cut, 52):
                temp_card.append(self.card[i])

            for i in range(0, cut):
                temp_card.append(self.card[i])
   
            self.card = temp_card

    def deal(self):
        if self.counter == 51:
            self.shuffle()
        self.counter += 1
        return(self.card[self.counter])
    
    def get_deck(self):
        return self.card
    
    def get_counter(self):
        return self.counter

