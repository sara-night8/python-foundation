import random
fort_number = random.randint(1,8)
lucky_num = random.randint(1, 100)
fort_text = ""
if fort_number ==1:
    fort_text = "Dogs have owners, cats have staff."
elif fort_number ==2:
    fort_text = "The fortune you seek is in another cookie"
elif fort_number == 3:
    fort_text = "About time I got out of that cookie."
elif fort_number == 4:
    fort_text = "Perseverance brings good fortune."
elif fort_number == 5:
    fort_text = "Carpe diem"
elif fort_number == 6:
    fort_text = "per aspera ad astera"
elif fort_number == 7:
    fort_text = "The snow may fall, but the sun also rises."
elif fort_number == 8:
    fort_text = "You were capable of imagining a different future. And maybe it won’t be realized today, maybe not in our lifetime."
else:
    fort_text = "Bd luck- empty cookie!"
print("CRACK! Your fortune is:")
print(f"\"{fort_text}\"")
print(f"Your Lucky Number for today is: {lucky_num}")