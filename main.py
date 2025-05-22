import sys
from datetime import datetime
from read import read_items, read_items_line
from operation import clear_stock, add_stock
from write import write_new_rent
import operation


def main():
   
    """
    read_items() is a function that converts text file into dictionary
    we are storing the dictionary in the variable named inventory
    
    """
   
    inventory= read_items("item.txt")
    # The system should run as long as it is open
    #and then close on exit 
    #Main menu display 
    
    print(" Babaji CENTER")
    print(" SHARINGAN |98XXXXXXX\n")
    loop=True
    while loop==True:
        #asks input from user
        try:
            print("Press 1 to Rent ")
            print("Press 2 to Return ")
            print("Press 3 to exit")
            userInput_valid = False
            while userInput_valid == False:
                try:
                    userInput=int(input("Enter a number to continue: "))
                    userInput_valid = True
                except ValueError:
                    print("Invalid user Input")
        except:
            print("Enter valid number")
        else:
            if userInput==1:
                operation.rent(inventory)
            elif userInput==2:
                operation.rental_return(inventory)
            # Exits the system, a fucntion from another library is imported for this
            elif userInput==3:
                print("Thanku for visting our store")
                sys.exit(0)
            else:
                print("Omae wa baka desu ne------- Enter the correct option-------")

main()
