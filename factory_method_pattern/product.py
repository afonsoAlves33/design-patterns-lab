from product_interface import IProduct


class ProductionDatabase(IProduct):
    def __init__(self):
        super().__init__()
        
    def operation(self):
        """
        This operation could have a more concrete name
        """
        return "(ProductionDatabase) [operation]: I am persisting a user in production database"
    
class TestsDatabase(IProduct):
    def __init__(self):
        super().__init__()
        
    def operation(self):
        """
        This operation could have a more concrete name
        """
        return "(TestsDatabase) [operation]: I am persisting a user in tests database"