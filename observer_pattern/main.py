from observer_pattern.observer import ShoppingCartGraphicInterface, ShoppingCartLogger
from observer_pattern.subject import ShoppingCartHandler


if __name__ == "__main__":
    # Observers
    web_graphic_interface = ShoppingCartGraphicInterface()
    mobile_graphic_interface = ShoppingCartGraphicInterface()
    shopping_cart_logger = ShoppingCartLogger()
    
    # Subject
    shopping_cart_handler = ShoppingCartHandler()
    
    shopping_cart_handler.attach(web_graphic_interface)
    shopping_cart_handler.attach(mobile_graphic_interface)
    shopping_cart_handler.attach(shopping_cart_logger)
    
    shopping_cart_handler.add_item("headphone")
    
    shopping_cart_handler.remove_item("headphone")
    
    shopping_cart_handler.add_item("keyboard")
    
    shopping_cart_handler.add_item("charger")
    
    
    
    