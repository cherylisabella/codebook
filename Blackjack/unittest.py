import unittest
from blackjack import Cards, Deck, Hand, BlackJack

class TestBlackjackGame(unittest.TestCase):

    def test_card_value(self):
        """Test card values (including ace, face cards, etc.)"""
        self.assertEqual(Cards.card_value['ace'], 11)
        self.assertEqual(Cards.card_value['king'], 10)
        self.assertEqual(Cards.card_value['2'], 2)

    def test_deck_initialization(self):
        """Test if a deck contains 52 cards and is properly initialized"""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertTrue(all(isinstance(card, Cards.OneCard) for card in deck.cards))

    def test_deck_shuffle(self):
        """Test if deck shuffle changes the card order"""
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(original_order, deck.cards)

    def test_deal_cards(self):
        """Test dealing one or more cards from the deck"""
        deck = Deck()
        dealt_cards = deck.deal(5)
        self.assertEqual(len(dealt_cards), 5)
        self.assertTrue(all(isinstance(card, Cards.OneCard) for card in dealt_cards))

    def test_hand_add_and_score(self):
        """Test adding cards to hand and calculating total value"""
        hand = Hand()
        hand.add_cards([Cards.OneCard('ace', 'hearts'), Cards.OneCard('jack', 'spades')])
        self.assertEqual(hand.total_value, 21)  # Ace + Jack = 21
        hand.add_cards([Cards.OneCard('ace', 'diamonds')])
        self.assertEqual(hand.total_value, 12)  # Second Ace counts as 1, total = 12

    def test_blackjack_bust(self):
        """Test if the player's hand busts when exceeding 21"""
        blackjack_game = BlackJack()
        blackjack_game.deck.cards = [
            Cards.OneCard('king', 'hearts'),
            Cards.OneCard('queen', 'hearts'),
            Cards.OneCard('jack', 'hearts')]
        blackjack_game.play()
        self.assertGreater(blackjack_game.hand.total_value, 21)

    def test_blackjack_game_flow(self):
        """Test the overall Blackjack game flow"""
        blackjack_game = BlackJack()
        blackjack_game.deck.shuffle()
        blackjack_game.play()
        self.assertGreaterEqual(blackjack_game.hand.total_value, 17)
        self.assertLessEqual(blackjack_game.hand.total_value, 21)

if __name__ == '__main__':
    unittest.main()
