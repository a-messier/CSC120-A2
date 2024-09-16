Use this file to record your reflection on this assignment. 

What worked, what didn't, what advice would you give someone taking this course in the future?

This assignment felt really difficult until I sat down and thought through the higher level structure of the classes. I wasn't sure how to interface the two classes at first, because I didn't have a strong grasp on how attributes could be accessed outside of a class. I understood that I could call the Computer() class to create an instance of a computer, and I would have to use that computer object within the ResaleShop class. I wasn't sure how to interface the two without the code looking clunky.

I finally landed on requiring a Computer object as input to the buy function of the ResaleShop class, so that the Computer object could be initialized in the main() function (outside of the ResaleShop class) from a list, and then the Computer object would be stored in the inventory of the ResaleShop class. 

I also struggled with how to use the ItemID variable. I thought about including the itemID as an optional attribute of the Computer class, but realized that may be too circular and maybe too complicated. I opted to let the user input the computer ID when selling/buying/refurbishing things, which makes things a lot simpler, but requires the user to know the ID of the computer in the inventory rather than different attributes of the computer. Since the inventory prints out frequently, this seemed like a reasonable assumption. 

Once I was able to design a working computer shop, I was able to copy over a lot of the functional code from the procedural file to the class file, and update most of the variables to be self.(variable) for the functions within the class. The main() function code was also very similar to the code in the main.py file, just updated to access functions from the ResaleShop() class. 

All in all, this assignment helped me get a grasp on how objects/classes can be interfaced in Python, and helped me understand how to translate a procedural process into one using objects. Since all the Python I have written in the past has been procedural (and looks a lot like the nested dictionary code from the procedural.py module), this assignment really helped me see the benefits of using classes over lots of nested dictionaries. 
