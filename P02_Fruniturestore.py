comfy_couch_description = "The Comfy Couch. 5 seater. 100% leather. 50 inches high x 65 inches wide x 40 inches dee. Comes in creamy white or cool baby blue."
comfy_couch_price = 3,865
super_spectecular_stellar_sofa_desc = "Super Spectecular Stellar Sofa. 100% leather on real birch. 30 x 41 x 30. Soothing Sage"
super_spectecular_stellar_sofa_price = 335
lightning_lava_lamp_desc = "Lightning Lava Lamp. Lights up any room. Strong glass and real wood. 40 in."
lightning_lava_lamp_price = 100
sales_tax = 0.088
cu_one_total = 0
cu_one_itemization = ""
cu_one_total+=comfy_couch_price
cu_one_itemization += comfy_couch_description + "\n"
cu_one_tax = cu_one_total * sales_tax
cu_one_total += cu_one_tax
print("\n" + "*"*30)
print ("   SUPER OFFICAL AND PROFESSIONAL RECIPT")
print("*"*30)
print("\nCUSTOMER ITEMS:")
print(cu_one_itemization)
print("-"* 30)
print(f"SUBTOTAL + TAX: ${cu_one_total:.2f}")
print("*"*30)
print("THANK YOU FOR SHOPPING!")
print("*"*30)