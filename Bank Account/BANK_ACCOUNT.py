import json


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        self.history.append(f"Withdrew {amount}")

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
        self.history.append(f"Transferred {amount} to {other.name}")

    def balance(self):
        return self._balance

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self._balance,
            "history": self.history
        }


def save_accounts(accounts, filename="accounts.json"):
    data = [a.to_dict() for a in accounts]

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_accounts(filename="accounts.json"):
    try:
        with open(filename) as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    accounts = []

    for d in data:
        acc = BankAccount(d["name"], d["balance"])
        acc.history = d["history"]
        accounts.append(acc)

    return accounts


# --- main ---

alice = BankAccount("Alice", 100)
bob = BankAccount("Bob", 50)

alice.deposit(50)
alice.transfer(bob, 30)

print(alice.name, alice.balance(), alice.history)
print(bob.name, bob.balance(), bob.history)

save_accounts([alice, bob])

loaded = load_accounts()

print(loaded[0].name, loaded[0].balance(), loaded[0].history)