favorites = {"color": "blue", "food": "sushi", "movie": "The Greatest Showman"}

def show_favorites(favs):
    print("Here are all your favorites: \n")
    for cat, val in favorites.items():
        print(f"{cat}: {val}")

def look_for_fav(favs):
    cat = input("Which category would you like to see? ")
    if cat in favorites:
        print(f"My favorite {cat} is {favorites[cat]}!")
    else:
        print("Sorry, that category is invalid.")

def add_fav(favs):
    cat = input("Enter a new category: ")
    if cat in favorites:
        print(f"The category {cat} already exists. ")
    else:
        val = input(f"Enter your favorite for {cat}: ")
        favorites[cat] = val

def update_fav(favs):
    cat = input("Enter a category to update: ")
    if cat in favorites:
        val = input(f"Enter your new favorite for {cat}: ")
        favorites[cat] = val
    else:
        print(f"The category {cat} does not exist. ")

def delete_fav(favs):
    cat = input("Enter a category to delete: ")
    if cat in favorites:
        del favorites[cat]
        print(f"The category {cat} has been deleted. ")
    else:
        print(f"The category {cat} does not exist. ")