
class Computer:
    
    # attributes taken from create_computer inputs 
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, # initilize variabes w inputs
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        
        self.description = description # add to self with same variable names 
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price
        
def main():
    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    print(computer.description)
    
if __name__ == "__main__":    # only call main if I am running this program directly # will not run if I import it 
    main()