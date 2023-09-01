# create a main function in main.py and import the Inventory class from inventory.py

from inventory import Inventory, Item

def main():
    inventory = Inventory()

    while True:
        print("\n INVENTORY MANAGEMENT SYSTEM \n")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item") 
        print("4. List items")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            item = Item(item, quantity)
            inventory.add_item(item)

        elif choice == 2:
            itemname = input("Enter item name: ")
            inventory.remove_item(itemname)

        elif choice == 3:
            item = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            item = Item(item, quantity)
            inventory.update_item(item)

        elif choice == 4:
            inventory.list_items()

        elif choice == 5:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()