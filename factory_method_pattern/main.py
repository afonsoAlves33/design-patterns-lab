from creator_interface import ICreator
from creator import UserTestsRepository, UserProductionRepository


def persist_user_in_db(creator: ICreator): # This ICreator could be called DatabaseCreator or anything that suitted better in a more concrete name definition
    """
    The client code (this def) works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client code: I'm not aware of the creator's class, but it still works. I'm Persisting a User data to the db:\n"
          f"{creator.operation()}")
    
    
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.)")
    persist_user_in_db(UserTestsRepository())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    persist_user_in_db(UserProductionRepository())