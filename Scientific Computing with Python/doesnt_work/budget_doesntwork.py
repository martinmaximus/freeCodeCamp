class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.total -= amount
            return True
        return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.total:
            return False
        return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + \
                f"{item['amount']:>7.2f}" + '\n'
        total = f"Total: {self.total:.2f}"
        return title + items + total
    
def create_spend_chart(categories):
    total = 0
    spent = []
    names = []
    for category in categories:
        total += category.total
        spent.append(0)
        for item in category.ledger:
            if item["amount"] < 0:
                spent[-1] += abs(item["amount"])
    for category in categories:
        names.append(category.name)
    for i in range(len(spent)):
        spent[i] = int(round(spent[i]/total, 2)*100)
    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)
    for label in labels:
        graph += f"{label:>3}| "
        for percent in spent:
            if percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"
    graph += "    ----" + ("---" * (len(categories) - 1))
    graph += "\n     "
    longest_name_length = 0
    for name in names:
        if longest_name_length < len(name):
            longest_name_length = len(name)
    for i in range(longest_name_length):
        for name in names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length-1:
            graph += "\n     "
    return graph


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
      
    def withdraw(self, amount, description=""):
      if self.check_funds(amount):
          self.ledger.append({"amount": -amount, "description": description})
          self.total -= amount
          return True
      else:
          return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        
    def check_funds(self, amount):
            if amount > self.total:
                return False
            return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + \
                     f"{item['amount']:>7.2f}\n"
        total = f"Total: {self.total}"
        return title + items + total


def create_spend_chart(categories):
  def create_spend_chart(categories):
    total = 0
    spent = []
    names = []
    for category in categories:
        total += category.total
        spent.append(0)
        names.append(category.name)
        for item in category.ledger:
            if item["amount"] < 0:
                spent[-1] += abs(item["amount"])
    if total == 0:  # Add a check for zero division
        return "Percentage spent by category\n" + "No data available"
    for i in range(len(spent)):
        spent[i] = int(round(spent[i]/total, 2)*100)
    graph = "Percentage spent by category\n"
    labels = range(100, -10, -10)
    for label in labels:
        graph += f"{label:>3}|"
        for spent_percent in spent:
            if spent_percent >= label:
                graph += "o  "
            else:
                graph += "   "
        graph += " \n"
    graph += "    ____" + ("___" * (len(categories) - 1))
    graph += "\n     "
    longest_name_length = 0
    for name in names:
        if longest_name_length < len(name):
            longest_name_length = len(name)
    for i in range(longest_name_length):
        for name in names:
            if i < len(name):
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length - 1:
            graph += "\n     "
    return graph            