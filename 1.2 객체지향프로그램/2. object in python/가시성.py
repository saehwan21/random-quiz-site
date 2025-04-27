class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.__items = []     #외부에서 못찾게함
        self.test = "abc"

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid item")
        
    def get_number_of_items(self):
        return len(self.__items)
    