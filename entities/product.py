class Product:
    def __init__(self, barcode, name, brand, price, quantity):
        self.__barcode = barcode
        self.__name = name
        self.__brand = brand
        self.__price = int(price)
        self.__quantity = int(quantity)
        
    def get_barcode(self):
        return self.__barcode
    
    def get_name(self):
        return self.__name
    
    def get_brand(self):
        return self.__brand
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def set_barcode(self, new_barcode):
        self.__barcode = new_barcode
        
    def set_name(self, new_name):
        self.__name = new_name
        
    def set_brand(self, new_brand):
        self.__brand = new_brand
        
    def set_price(self, new_price):
        self.__price = new_price
        
    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity
        
    def substract_quantity(self, given_quantity):
        self.__quantity -= given_quantity
        
    def __eq__(self, other):
        return self.__barcode == other.get_barcode()
    
    def __str__(self):
        return "Barcode {0}, Name {1}, Brand {2}, Price {3}, Quantity {4}".format(self.__barcode, self.__name, self.__brand, self.__price, self.__quantity)
    
    def __repr__(self):
        return str(self) + "__repr__"