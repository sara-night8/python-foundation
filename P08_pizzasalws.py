toppings = ["choco shavings", "gummy bears", "snickers", "mnms", "choco chips", "whip cream"]
prices = [.25, .50, .75, .50,.25, .20]
num_ice =len(toppings)
print(f"We have [num_ice] toppings available to add on or mix in to your scrumptious ice cream all for a low charge!")
icec = list(zip(prices,toppings))
print("\nUnsorted Ice Cream(prices,toppings):")
print(icec)
icec.sort()
print("\nSorted Menu:")
print(icec)
cheapest = icec[0]
priciets = icec[-1]
threecheap = icec[:3]
print(f"\nCheapest option: {cheapest}")
print(f"\nPriciest option: {priciets}")
print(f"Budget Option:{threecheap}")