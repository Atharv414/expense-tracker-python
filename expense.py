class Expense:

    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def display(self):
        print(f"Date: {self.date}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Amount: ₹{self.amount:.2f}")

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["date"],
            data["category"],
            data["description"],
            data["amount"]
        )