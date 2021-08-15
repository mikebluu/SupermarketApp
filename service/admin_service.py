#THIS IS DONE
from domain.product import Product
from repository.repository import Repository


class AdminService:
    def __init__(self, product_repository: Repository):
        self.__product_repository = product_repository
        
    def add(self, barcode, name, brand, price, quantity):
        self.__product_repository.add(Product(barcode, name, brand, price, quantity))
    
    def delete(self, barcode):
        self.__product_repository.delete(Product(barcode, 0, 0, 0 , 0))
        
    def get_all(self):
        return self.__product_repository.get_all_products()
    
    def modify(self, barcode, new_name, new_brand, new_price, new_quantity):
        product_list = self.__product_repository.get_all_products()
        for product in product_list:
            if product.get_barcode() == barcode:
                product.set_name(new_name)
                product.set_brand(new_brand)
                product.set_price(new_price)
                product.set_quantity(new_quantity) 
            
       
    def get_brand(self, brand):
        product_list = self.__product_repository.get_all_products()
        for product in product_list:
            if product.get_brand() == brand:
                print(product)
       
