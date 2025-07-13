# Blackjack Game

This is a simple implementation of a **Blackjack** card game using Python. The game allows the player to interact with the deck, draw cards, and simulate a basic Blackjack round where the player keeps drawing cards until their hand's total value is at least 17.

Note: This project was developed as one of my homework submissions for a **16-hour undergraduate Python course**.

## Requirements

- Python 3.x
- No external libraries required (relies on built-in `random` module)

## Overview

The game is composed of four main classes:
1. **Cards**: Represents a collection of playing cards. Each card has a rank and a suit (e.g., Ace of Spades).
2. **Deck**: A collection of 52 cards, with methods to shuffle and deal cards.
3. **Hand**: Represents the player's hand of cards. It includes methods to add cards and calculate the hand's total score, handling Aces as both 1 or 11.
4. **Blackjack**: The game logic. It creates a deck, deals cards to the player, and simulates the player's turn until they reach a total hand value of 17 or higher.

## UML Diagram

Below is a **UML diagram** that illustrates the relationships between the classes:

```mermaid
classDiagram
    class Cards {
        - ranks: list
        - suits: list
        - card_value: dict
    }

    class OneCard {
        - rank: str
        - suit: str
    }

    Cards --> OneCard : "Has"
    Cards <|-- Deck
    Cards <|-- Hand
    Deck --> BlackJack : "Contains"
    Hand --> BlackJack : "Contains"

    class Deck {
        + shuffle()
        + deal()
    }

    class Hand {
        - total_value: int
        - contains_ace: bool
        + add_cards()
        + score()
    }

    class BlackJack {
        - deck: Deck
        - hand: Hand
        + play()
    }
