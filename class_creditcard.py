class CreditCard:

    def __init__(self, holder_name, card_number):
        self.holder_name = holder_name
        self.card_number = card_number

    def pay(self, amount):
        print(
            f"[CreditCard] {self.holder_name} "
            f"paid {amount} via card {self.card_number}"
        )

class UPI:

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(
            f"[UPI] {self.upi_id} paid {amount}"
        )

class Cash:

    def __init__(self, person_name):
        self.person_name = person_name

    def pay(self, amount):
        print(
            f"[Cash] {self.person_name} paid {amount} in cash"
        )

def checkout(payment_method, amount):
    payment_method.pay(amount)

methods = [
    CreditCard("Alice", "4111-1111-1111-1111"),
    UPI("bob@upi"),
    Cash("Carol")
]
for method in methods:
    checkout(method, 500)