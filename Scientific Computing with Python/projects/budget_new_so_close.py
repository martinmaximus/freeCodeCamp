def create_spend_chart(categories):

    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))
  
    # Calculate percentage rounded down to the nearest 10
    total = sum(spent_amounts)
    spent_percentages = [int((amount / total) * 100) for amount in spent_amounts]
  
  
    # Create header
    header = "Percentage spent by category" 

    # Create body
    
    body = str()
    
    for percentage in range(100, -10, -10):
        body += str(percentage).rjust(3) + "| "
        for spent_percentage in spent_percentages:
            if spent_percentage >= percentage:
                body += "o  "
            else:
                body += "   "
        body += "\n"
    

    # Create footer
    footer = "    " + "_"*10
    descriptions = [category.name for category in categories]
    max_length = max(len(name) for name in descriptions)
    descriptions = [name.ljust(max_length) for name in descriptions]

  
    return (header + body + footer).rstrip("\n").rstrip()


class Category:
  def __init__(self, name):
      self.name = name
      self.ledger = list()

  def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
      if self.check_funds(amount):
          self.ledger.append({"amount": -amount, "description": description})
          return True
      else:
          return False

  def get_balance(self):
      total_cash = 0
      for item in self.ledger:
          total_cash += item["amount"]
      return total_cash

  def transfer(self, amount, category):
      if self.check_funds(amount):
          self.withdraw(amount, f"Transfer to {category.name}")
          category.deposit(amount, f"Transfer from {self.name}")
          return True
      else:
          return False

  def check_funds(self, amount):
      if amount > self.get_balance():
          return False
      else:
          return True

  def __str__(self):
      title = f"{self.name:*^30}\n"
      items = ""
      total = 0
      for item in self.ledger:
          items += f"{item['description'][:23]:23}" + \
                   f"{item['amount']:>7.2f}\n"
          total += item['amount']

      output = title + items + "Total: " + str(total)
      return output


