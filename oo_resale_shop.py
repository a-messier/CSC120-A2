from computer import Computer # imports computer class from computer.py

global itemID # I tink this goes here?
itemID = 0 

class ResaleShop:
    # What attributes will it need?
    inventory: dict
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = {} # initlizes empty dictionary to add computers to 
        
    # What methods will you need?
    def buy(self, computer: Computer): # argument as computer class 
        global itemID
        itemID+=1 # increases item ID for new computer 
        # adds computer object to inventory dictionary with key 
        self.inventory[itemID] =  computer
        
    # updates price of computer 
    def update_price(self, ID:int, new_price:int):
        computer = self.inventory[ID] # accesses computer of interest from inventory
        computer.price = new_price # assigns new price in place of old price
        
        if ID not in self.inventory.keys(): # checks to see if ID is in inventory 
            print(f"Item {ID} not found. Cannot update price.") # prints warning if ID not present 
            
    # sell computer 
    def sell(self, ID:int): # pass computer ID 
        del self.inventory[ID] # removes from inventory based on item ID 
    
    # prints store inventory 
    def print_inventory(self):
        if self.inventory: # if inventory is not empty 
             for item_id in self.inventory: # iterates over computers in inventory
                print(f'Item ID: {item_id} : {vars(self.inventory[item_id])}') # vars prints out attributes + values of class object 
        else:
            print("No inventory to display.")

    # refurbish function 
    def refurbish(self, ID:int, new_os = None): # optional new OS keyword  
        if ID in self.inventory: # checks to see if computer is in inventory 
            computer = self.inventory[ID] # assigns computer object to a variable 
            
            if int(computer.year_made) < 2000: # checks if made before 2000, should already be int
                computer.price = 0 # sets to 0 
            
            elif int(computer.year_made) < 2012: # "", 2012
                computer.price = 250 

            elif int(computer.year_made) < 2018: # "", 2018
                computer.price = 550
                
            else: # "", anything after 2018 
                computer.price = 1000 
                
            if new_os: # checks to see if new_os is included as input 
                computer.operating_system = new_os # assigns new_os string to operating_system attribute 
            
        else: # if ID not present in inventory, raises issue 
            print("Item", ID, "not found. Please select another item to refurbish.")

def main():
    
        # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    
    # initilizes shop from ResaleShop object 
    shop = ResaleShop() 
    # test computer list, creates computer object 
    test_computer = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000) # makes test computer object
    
    # buys computer 
    print("Buying", test_computer.description)
    print("Adding to inventory...")
    shop.buy(test_computer) # buys test_computer
    print(f"Item added to inventory at Item ID {itemID}")
    print("Done.\n")
    
    # checks inventory 
        # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Refurbushes computer 
        # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", itemID, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(itemID, new_OS)
    print("Done.\n")
    
        # checks inventory 
        # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # sells computer 
    print("Selling Item ID:", itemID)
    shop.sell(itemID)
    
            # checks inventory 
        # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

main()