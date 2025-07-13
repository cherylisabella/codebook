import random

class Cards:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    suits = ["clubs", "diamonds", "hearts", "spades"]
    card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "jack": 10, "queen": 10, "king": 10, "ace": 11}

    class OneCard:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

        def __str__(self):
            return f"{self.rank} of {self.suit}"

class Deck(Cards):
    def __init__(self):
        self.cards = [self.OneCard(rank, suit) for rank in self.ranks for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n):
        return [self.cards.pop(0) for _ in range(n)]

    def sort_rank(self):
        """Sort cards by rank in the order of Cards.ranks"""
        rank_order = {rank: index for index, rank in enumerate(self.ranks)}
        self.cards.sort(key=lambda card: rank_order[card.rank])

    def sort_suit(self):
        """Sort cards by suit in the order of Cards.suits"""
        suit_order = {suit: index for index, suit in enumerate(self.suits)}
        self.cards.sort(key=lambda card: suit_order[card.suit])

class Hand(Cards):
    def __init__(self):
        self.cards = []
        self.total_value = 0
        self.contains_ace = False

    def add_cards(self, new_cards):
        for card in new_cards:
            self.cards.append(card)
            value = self.card_value[card.rank]
            if value == 11 and self.total_value + 11 > 21:
                value = 1  # Ace is counted as 1 if it would bust
            self.total_value += value
            if card.rank == 'ace':
                self.contains_ace = True

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()

    def play(self):
        self.deck.shuffle()
        self.hand.add_cards(self.deck.deal(2))  # Deal two cards
        while self.hand.total_value < 17:  # Continue adding cards if total is less than 17
            self.hand.add_cards(self.deck.deal(1))
        self.show_result()

    def show_result(self):
        print(f"Your hand: {', '.join(str(card) for card in self.hand.cards)}")
        if self.hand.total_value > 21:
            print(f"Total value: {self.hand.total_value} - Bust! You lose.")
        else:
            print(f"Total value: {self.hand.total_value} - You stand.")

# To play the game
if __name__ == '__main__':
    game = BlackJack()
    game.play()
