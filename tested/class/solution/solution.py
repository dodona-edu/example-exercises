class Counter:
    def __init__(self, beginwaarde=0):
        self.teller = beginwaarde

    def count(self):
        self.teller += 1
        return self

    def report(self):
        print(self.teller)
