# create Item class and inventory class in inventory.py

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item.name] += item.quantity
        else:
            self.inventory[item.name] = item.quantity

    def remove_item(self, itemname):
        if itemname in self.inventory:
            print("Item removed from inventory")
            del self.inventory[itemname]
        else:
            print("Item not found in inventory")

    def update_item(self, item):
        if item.name in self.inventory:
            self.inventory[item.name] = item.quantity
        else:
            print("Item not found in inventory")
    
    def list_items(self):
        return self.inventory

