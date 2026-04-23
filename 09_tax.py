def calculate_total(price, tax_rate):
    tax_amount = price * tax_rate
    total = price + tax_amount
    print(f"The final price with tax is: ${total:2f}")
    calculate_total(800.09,0.98)
    calculate_total(54.90,666)