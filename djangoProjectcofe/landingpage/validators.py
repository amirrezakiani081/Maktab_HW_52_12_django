from django.core.exceptions import ValidationError
def price_menu_validator(val):
    if val < 0:
        raise ValidationError('menu item price cant be negetive')