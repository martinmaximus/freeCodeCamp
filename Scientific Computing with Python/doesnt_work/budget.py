class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0.0
    
    def represent(self):
        header = self.description.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            # format ndescription and amount
            line_description = item["description"][:23].ljust(23)
            line_amount = "{:.2f}".format(item["amount"][:7]).rjust(7)
            # add line to ledger
            ledger += line_description + line_amount + "\n"
        # format total
        total = "Total: {:.2f}".format(self.balance)
        # return header + ledger + total
        return header + ledger + total
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.description)
            category.deposit(amount, "Transfer from " + self.description)
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    spent_amounts = []
    # get total spent for each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded to nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentages = list(map(lambda amount: int(round(amount/total, 2)*100), spent_amounts))

    # Create the bar chart lines
    header = "Percentage spent by category\n"

    # Create the labels
    labels = []
    for i in range(100, -10, -10):
        labels.append(str(i).rjust(3) + "| ")
        for percent in spent_percentages:
            if percent >= i:
                labels[-1] += "o  "
            else:
                labels[-1] += "   "
        labels[-1] += "\n"

    
    