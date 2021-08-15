#THIS IS DONE
from exception.exceptions import ValidationError


class Validator:
    def __init__(self) -> None:
        super().__init__()
        
    def validate_barcode(self, barcode):
        if len(str(barcode)) > 10:
            raise ValidationError("Product barcode is longer than 10 characters, try again.")
    
    def validate_price(self, price):
        try:
            int_price = int(price)
        except Exception:
            raise ValidationError("Product price is not a number, try again.")
    
    def validate_quantity(self, quantity):
        try:
            int_quantity = int(quantity)
        except Exception:
            raise ValidationError("Product quantity is not a number, try again.")
            
        