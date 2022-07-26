class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits = {'Diamonds': '\u2666', 'Hearts': '\u2665', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return f"{self.value}{suits[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            self.cards += [Card(value, suit) for value in values]
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self):
        print(f"cards[{len(self.cards)}]{', '.join([card.to_str() for card in self.cards])}")
        # TODO-2: Принцип работы данного метода прописан в 00_task_deck.md



# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
