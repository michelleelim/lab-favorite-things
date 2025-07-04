favorites = {"color": "blue", "food": "sushi", "movie": "The Greatest Showman"}
print("Your favorite categories are:", ", ".join(favorites.keys()))

cat = input("Which category would you like to see? ")
if cat in favorites:
    print(f"My favorite {cat} is {favorites[cat]}!")
else:
    print("Sorry, that category is invalid.")

ans = input("Would you like to add a new favorite category? (yes/no) ")
if ans == "yes":
    new_cat = input("Enter new category: ")
    new_val = input(f"Enter your favorite for {new_cat}: ")
    favorites[new_cat] = new_val

print("Here are all your favorites: \n")
for cat, val in favorites.items():
    print(f"{cat}: {val}")
