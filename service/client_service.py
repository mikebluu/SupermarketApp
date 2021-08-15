from domain.product import Product
from repository.repository import Repository


class ClientService:
    def __init__(self, product_repository: Repository):
        self.__product_repository = product_repository
        
    def buy_product(self, name, quantity):
        product_list = self.__product_repository.get_all_products()
        for product in product_list:
            if product.get_name() == name:
                int_quantity = int(quantity)
                if int_quantity < product.get_quantity():
                    product.substract_quantity(int_quantity)
                    
    def show_cheaper_than(self, str_price):
        products_list = self.__product_repository.get_all_products()
        products_less_than_list = []
        for product in products_list:
            int_price = int(str_price)
            if product.get_price() < int_price:
                products_less_than_list.append(product)
        products_less_than_list = sorted(products_less_than_list, key=lambda product1: product1.price, reverse=True)
        for sorted_product in products_less_than_list:
            print(sorted_product)
                

        
