# write unit tests for inventory.py

import unittest
import sys

sys.path.append('../src')

from inventory import Inventory, Item

class TestInventory(unittest.TestCase):
    
    def setUp(self):
        self.inventory = Inventory()

    def test_add_item(self):
        item = Item("abc", 10)
        self.inventory.add_item(item)
        self.assertEqual(self.inventory.inventory, {"abc": 10})
    
    def test_remove_item(self):
        item = Item("abc", 10)
        self.inventory.add_item(item)
        self.inventory.remove_item(item.name)
        self.assertEqual(self.inventory.list_items(), {})

    def test_update_item(self):
       item = Item("jkl", 20)
       self.inventory.add_item(item)
       item1 = Item("jkl", 30)
       self.inventory.update_item(item1)
       self.assertEqual(self.inventory.inventory, {"jkl": 30})

    def test_list_items(self):
        item = Item("abc", 10)
        self.inventory.add_item(item)
        self.assertEqual(self.inventory.list_items(), {"abc": 10})


if __name__ == "__main__":
    unittest.main()
