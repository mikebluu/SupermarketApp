from entities.product import Product
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
    
    def show_cheaper_than(self, price):
        product_list = self.__product_repository.get_all_products()
        list_of_products_less_than = []
        for product in product_list:
            price = int(price)
            if product.get_price() < price:
                list_of_products_less_than.append(product)
            list_of_products_less_than.sort(key=lambda x: x.price, reverse=True)
        for sorted_product in list_of_products_less_than:
            print(sorted_product)

                

        
