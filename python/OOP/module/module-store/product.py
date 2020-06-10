class Product:
    def __init__(self, price, item, brand, cost, status):
        self.price = price
        self.item = item
        self.brand = brand
        self.cost = cost
        self.status = status
        
    def display_info(self):
        print(f"Price: {self.price}, \n Item: {self.item}. \n  Brand: {self.brand}, \n  Cost: {self.cost}, \n Status: {self.status} \n ")

# if __name__ == "__main__":
#     product1 = Product(99.99, "C922 Pro Stream Webcam", "Logitech", 300, "n/a")
#     product1.display_info()
#     product1.Return("opened")



