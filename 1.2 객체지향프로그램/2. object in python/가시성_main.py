from 가시성 import Product
from 가시성 import Inventory

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory.get_number_of_items())


print("_______________")
print(my_inventory.__items)
my_inventory.add_new_item(object)