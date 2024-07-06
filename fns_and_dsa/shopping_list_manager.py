def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            new_item = input("what is the new item you want to add? ")
            shopping_list.append(new_item)
            pass
        elif choice == '2':
            removed_item = input("what is the item you want to remove? ")
            if shopping_list.__contains__(removed_item):
                shopping_list.remove(removed_item)
            else: 
                print("choose an item from the shopping list")
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()