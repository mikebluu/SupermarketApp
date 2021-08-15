#THIS IS DONE
from exception.exceptions import NotFoundException, DuplicateException, NoProductsException


class Repository:
    def __init__(self):
        self.__entities_list = []
        
    def __find_position(self, entity):
        for i in range(len(self.__entities_list)):
            if self.__entities_list[i] == entity:
                return i
            return None
    
    def add(self, new_entity):
        if self.__find_position(new_entity) is not None:
            raise DuplicateException(new_entity)
        self.__entities_list.append(new_entity)
        
    def delete(self, entity):
        position = self.__find_position(entity)
        if position is None:
            raise NotFoundException(entity)
        del self.__entities_list[position]
        
    def get_all_products(self):
        if len(self.__entities_list) == 0:
            raise NoProductsException()
        return self.__entities_list
    
