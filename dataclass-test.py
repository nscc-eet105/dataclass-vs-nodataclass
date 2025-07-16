from dataclasses import dataclass

class Parent_No_Dataclass:
    def __init__(self, parent_value=0.0):
        self.__parent_value = parent_value

    def __str__(self):
        return f"__parent_value={self.__parent_value:.2f}"
    
    # NOTE: @property does not require dataclass
    @property
    def parent_value(self):
        return self.__parent_value

class Child_No_Dataclass(Parent_No_Dataclass):
    def __init__(self, parent_value=0.0, child_value=0.0):
        super().__init__(parent_value)
        self.__child_value = child_value
    
    def __str__(self):
        return f"__parent_value={self.parent_value:.2f}\n__child_value={self.__child_value:.2f}"

@dataclass
class Parent_Dataclass:
    # Define the instance attributes as follows:
    __parent_value:float = 0.0

    # No __init__ is needed as @dataclass automaticaly generates basically the same thing done manually above
    
    # @property still must be manually created
    @property
    def parent_value(self):
        return self.__parent_value
    
    # No __str__ is needed as @dataclass automatically generates a __ref__ which is very similar to __str__

@dataclass
class Child_Dataclass(Parent_Dataclass):
    # Define the instance attributes as follows:
    __child_value:float = 0.0

    # No __init__ is needed as @dataclass automaticaly generates basically the same thing done manually above
    # No __str__ is needed as @dataclass automatically generates a __ref__ which is very similar to __str__
    
    
def main():
    # Test No_Datacclass
    parent_variable_no_dataclass = Parent_No_Dataclass(1.111)
    print(parent_variable_no_dataclass)
    print(f"{parent_variable_no_dataclass.parent_value:.2f}")
    child_variable_no_dataclass = Child_No_Dataclass(2.222, 3.333)
    print(child_variable_no_dataclass)
    print(f"{child_variable_no_dataclass.parent_value:.2f}")
    # Test Datacclass
    parent_variable_dataclass = Parent_Dataclass(4.444)
    print(parent_variable_dataclass)
    print(f"{parent_variable_dataclass.parent_value:.2f}")
    child_variable_dataclass = Child_Dataclass(5.555, 6.666)
    print(child_variable_dataclass)
    print(f"{child_variable_dataclass.parent_value:.2f}")
    
if __name__ == "__main__":
    main()