class Money :
    def __init__(self, amount) :
        self.amount = amount
        self.currency = "EUR"

    def __add__(self, other) :
        if self.currency != other.currency :
            raise ValueError("Mismatched currencies!")
        else :
            return Money(self.amount + other.amount, self.currency)
        
    def __sub__(self, other) :
        if self.currency != other.currency :
            raise ValueError("Mismatched currencies!")
        else :
            return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, factor) :
        return Money(self.amount * factor, self.currency)
        
        