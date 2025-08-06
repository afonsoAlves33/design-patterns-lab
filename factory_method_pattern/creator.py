from creator_interface import ICreator
from product import ProductionDatabase, TestsDatabase
from product_interface import IProduct


class UserProductionRepository(ICreator): # in production
    def __init__(self):
        super().__init__()
    
    def factory_method(self) -> IProduct:
        """
        This should be called 'factory_database' or anything more concrete, but it should be specified on the interface 
        (The interface should be more concrete, for instance: DatabaseCreator)
        """
        return ProductionDatabase()
    
    def operation(self):
        return super().operation()
    
    
class UserTestsRepository(ICreator):
    def __init__(self):
        super().__init__()
    
    def factory_method(self) -> IProduct:
        return TestsDatabase()
    
    def operation(self):
        return super().operation()
    
    
        
        
        