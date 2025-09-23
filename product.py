class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
   # def get_product_info(self):
       # return self.name, self.price


my_product = Product("Lenovo", 4000)
print(my_product.get_name)