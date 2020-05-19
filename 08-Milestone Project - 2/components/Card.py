class Card():
    def __init__(self, suite, order):
        # define card suite
        self.suite = suite
        # define card number/face
        self.order = order
        # if card is a face card, it has a value of 10
        if order in ['jack', 'queen', 'king']:
            self.value = 10
        # if card is an ace, the human player can choose a value of 1 or 11
        # therefore it's marked as -1
        elif order == 'ace':
            self.value = -1
        # any other card has its normal assigned
        else:
            self.value = order

    def get_suite(self):
        return self.suite

    def get_order(self):
        return self.order

    def get_value(self):
        return self.value
