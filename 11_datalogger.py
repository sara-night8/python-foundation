with open("snaks.txt", "w") as file:
  file.write("Milkyways: available\n")
  file.write("dried mango: available\n")
  file.write("popcorn: unavailable\n")
  file.write("fruit splits: available\n")
  file.write("bell peppers: unavailable\n")

  print("---FETCHING SNACK MENU---")
  with open("snaks.txt", "r") as file:
    for line in file:
      print(line.strip())