import json

# Function to load the shopping list from a JSON file
def load_shopping_list():
    try:
        with open("shopping_list.json", "r") as file:
            shopping_list = json.load(file)
    except FileNotFoundError:
        shopping_list = []
    return shopping_list

# Function to save the shopping list to a JSON file
def save_shopping_list(shopping_list):
    with open("shopping_list.json", "w") as file:
        json.dump(shopping_list, file)

# Function to add an item to the shopping list
def add_item(shopping_list):
    item = input("Enter the item to add to the shopping list: ")
    shopping_list.append(item)
    save_shopping_list(shopping_list)
    print(f"{item} has been added to the shopping list.")

# Function to remove an item from the shopping list
def remove_item(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
        
        try:
            idx = int(input("Enter the number of the item to remove: ")) - 1
            if 0 <= idx < len(shopping_list):
                removed_item = shopping_list.pop(idx)
                save_shopping_list(shopping_list)
                print(f"{removed_item} has been removed from the shopping list.")
            else:
                print("Invalid item number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to display the shopping list
def display_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")

# Main function to interact with the user
def main():
    shopping_list = load_shopping_list()

    while True:
        print("\nShopping List")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display List")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            display_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
