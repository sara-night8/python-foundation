def start_room():
    print("\n---THE GATE OF THE BIG ROCK CANDY MOUNTAIN ---")
    print("You stand before the gatekeeper of this sacred land. He is sleeping and in a deep sleep")
    choice = input("Do you [1] Wake him up or [2] sneek")
    if choice == "1":
        print("He wakes up and is angry. You better run!")
        return "end"
    else:
        print("You made it to the bridge. YOUR FREE ENJOY A SCLICE OF AWESOMNESS")
def treasure_room():
    print("\n---THE CANDY VAULT---")

print("Candy rains down.")
current_room = "start"
print("Welcome to the Python Adventure Engine!")
while current_room !="end":
    if current_room == "start":
        current_room = start_room()
    elif current_room == "treasure_room":
            current_room = treasure_room ()

