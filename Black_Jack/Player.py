class Player:
    
    def __init__(self, cards_and_value=None):
        if cards_and_value is not None:
            self.cards = cards_and_value[0]
            self.card_value = cards_and_value[1]
        else:
            self.cards = []
            self.card_value = 0

    """def set_dealer(self):
        self.is_dealer = True
    """

    def add_cards(self, card):
        append_card = card
        
        if card[0] in (11, 12, 13):
            self.card_value += 10
        elif card[0] == 1:
            self.card_value += 11
            append_card = (14, card[1])
        else:
            self.card_value += card[0]

        self.cards.append(append_card)

        if self.card_value > 21:
            for i in range(0, len(self.cards)):
                if self.cards[i][0] == 14:
                    self.card_value -= 10
                    self.cards[i] = (1, self.cards[i][1])
                    break
            if self.card_value > 21:
                self.card_value = -1
                return "exceed"
            
        return "under"

    def peak_deck(self):
        result = []
        for x in self.cards:
            if x[0] == 14:
                result.append((1, x[1]))
            else:
                result.append(x)

        return result
    
    def peak_value(self):
        return self.card_value
    
    def reset(self):
        self.cards = []
        self.card_value = 0

    def calculate_cards_value(self):
        value = 0
        for card in self.cards:
            if card[0] in (11, 12, 13):
                value += 10
            elif card[0] == 14:
                value += 11
            else: 
                value += card[0]

        return value
