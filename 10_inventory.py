inventory = ["popcorn","brownies","dried mango"]
print(f"Unavailable snacks:{inventory[0]}")
inventory.append("freeze dried strawberries")
inventory.insert(1,"pretzels")
inventory.pop(0)
print(f"Curent Stock:{inventory}")