from favorite_things_functions import (
    favorites,
    look_for_fav,
    add_fav,
    update_fav,
    delete_fav,
    show_favorites
)

def main():
    while True:
        print("Your available categories are:", ", ".join(favorites.keys()))
        action = input("What would you like to do? (lookup/add/update/delete/quit): ")

        if action == "lookup":
            look_for_fav(favorites)
        elif action == "add":
            add_fav(favorites)
        elif action == "update":
            update_fav(favorites)
        elif action == "delete":
            delete_fav(favorites)
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
