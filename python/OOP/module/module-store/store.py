from product import Product
class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        items_in_store = best_buy.products.index(product) 
        self.products.pop(items_in_store)
        print(f"!!!!! removing !!!!!  {product.item}")
        return self

    def inventory(self):
        print (f"====== {self.name} ======")
        for i in range(0,len(self.products)):
            print (self.products[i].display_info())

best_buy = Store("Best buy")

# if you are from the future compare the prices from today is 06-04-20
product1 = Product(99.99, "C922 Pro Stream Webcam", "Logitech", 300, "n/a")
product2 = Product(199.99, "4K Pro Webcam", "Logitech", 300, "2")
product3 = Product(69.99, "C920S HD Webcam", "Logitech", 300, "sale")
best_buy.add_product(product1)
best_buy.add_product(product2)
best_buy.add_product(product3)
best_buy.inventory()
print("* *"*70)
best_buy.remove_product(product2)
best_buy.inventory()


