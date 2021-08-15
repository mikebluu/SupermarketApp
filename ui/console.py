from exception.exceptions import ProgramError
from service.admin_service import AdminService
from service.client_service import ClientService
from validator.validator import Validator


class UI:
    def __init__(self, admin_service: AdminService, client_service: ClientService):
        self.__admin_service = admin_service
        self.__client_service = client_service
        self.__validator = Validator()
    
    def __add_product(self):
        barcode = input("Enter barcode: ")
        self.__validator.validate_barcode(barcode)
        name = input("Enter name: ")
        brand = input("Enter brand: ")
        price = input("Enter price: ")
        self.__validator.validate_price(price)
        quantity = input("Enter quantity: ")
        self.__validator.validate_quantity(quantity)
        self.__admin_service.add(barcode, name, brand, int(price), quantity)
        
    def __print_all_products(self):
        for product in self.__admin_service.get_all():
            print(product)
            
    def __delete_product(self):
        barcode = input("Barcode of product to be deleted: ")
        self.__validator.validate_barcode(barcode)
        self.__admin_service.delete(barcode)
        
    def __modify_product(self):
        barcode = input("Barcode of product to be modified: ")
        self.__validator.validate_barcode(barcode)
        new_name = input("New name of product to be modified: ")
        new_brand = input("New brand of product to be modified:")
        new_price = input("New price of product to be modified: ")
        self.__validator.validate_price(new_price)
        new_quantity = input("New quantity of product to be modified: ")
        self.__validator.validate_quantity(new_quantity)
        self.__admin_service.modify(barcode, new_name, new_brand, new_price, new_quantity)
        
    def __get_brand(self):
        brand = input("Brand of the products to be shown: ")
        self.__admin_service.get_brand(brand)
        
    def __buy_product(self):
        name = input("Name of product to be bought: ")
        quantity = input("How many products to be bought: ")
        self.__validator.validate_quantity(quantity)
        self.__client_service.buy_product(name, quantity)
        
    def __print_products_cheaper_than(self):
        price = input("Products will be cheaper than: ")
        self.__validator.validate_price(price)
        self.__client_service.show_cheaper_than(price)
        
        
    def __admin_menu(self):
        while True:
            print("1. Add product")
            print("2. Remove product")
            print("3. Modify product")
            print("4. Show all products")
            print("5. Show all products from a brand")
            print("0. Go back to main menu")
            try:
                command = int(input("What do you want to do? Choose from the commands: ").strip())
                if command == 0:
                    self.__main_menu()
                elif command == 1:
                    self.__add_product()
                elif command == 2:
                    self.__delete_product()
                elif command == 3:
                    self.__modify_product()
                elif command == 4:
                    self.__print_all_products()
                elif command == 5:
                    self.__get_brand()
            except ProgramError as error:
                print(error)
    
    def __client_menu(self):
        while True:
            print("1. Show all products")
            print("2. Buy a product")
            print("3. Show all products cheaper than ...")            
            print("0. Go back to main menu")
            try:
                command = int(input("What do you want to do? Choose from the commands: ").strip())
                if command == 0:
                    self.__main_menu()
                elif command == 1:
                    self.__print_all_products()
                elif command == 2:
                    self.__buy_product()
                elif command == 3:
                    # self.__print_products_cheaper_than()
                    print("Sorry! That isn't working at the moment.")
            except ProgramError as error:
                print(error)

    def __main_menu(self):
        while True:
            print("1. Enter Admin mode (DANGEROUS)")
            print("2. Enter Client mode (SAFE)")
            print("0. Exit :(")
            try:
                command = int(input("What do you want to do? Choose from the commands: ").strip())
                if command == 0:
                    exit()
                elif command == 1:
                    self.__admin_menu()
                elif command == 2:
                    self.__client_menu()
            except ProgramError as error:
                print(error)
                
    def run(self):
        while True:
            self.__main_menu()
