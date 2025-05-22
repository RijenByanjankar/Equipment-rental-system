from read import read_items
import write
from datetime import datetime
import read

inventory= read_items("item.txt")

def clear_stock(proper_id,user_quantity):
    inventory[proper_id][3]=int(inventory[proper_id][3])-int(user_quantity)
    #x=x-1
    return inventory

#adding stock on return
def add_stock(proper_id,user_quantity):
    inventory[proper_id][3]=int(inventory[proper_id][3])+int(user_quantity)
    #x=x+1
    return inventory


# Set the day for 5.meaning no fine will be charged until day 5
days = 5
def rent(inventory):
    name=input("Customer's name:   ")
    loop=True
    while loop==True:
        try:

            phoneNumber=int(input("Phone Number: "))
            loop=False
        except ValueError:
            print("invalid phone number")

    print("-------------------------------------------------------------------------------------------------\n")
    print("-------------------------------------------------------------------------------------------------")
    print("S.N. \t\t item Name      Brand Name     Price\t     Quantity")
    print("--------------------------------------------------------------------------------------------------")
    unique_id = name + str(phoneNumber)
    
    
    lines_of_inventories= read.read_items_line('item.txt')
    i=1
    for table_line in lines_of_inventories:
        
        print(i,"\t\t"+table_line.replace(',','\t'))
        i=i+1
    print('---------------------------------------------------------------------------------------------------')
    dict_for_user_bought_product=[]
    
    exiter = True
    while exiter == True: 
        stock_id_valid = False
        while stock_id_valid == False:
            try:   
                stock_id=int(input("Stock ID Number:"))
                stock_id_valid = True
            except ValueError:
                print("Enter valid ID!")
        print("\n")
        while stock_id<=0 or stock_id> len(inventory):
        
            print("Enter a valid stock ID!!!!!!!\t")
            stock_id=int(input("Stock ID Number: "))
        user_quantity_valid = False
        while user_quantity_valid == False:
            try:
                user_quantity=int(input("Stock Quantity: \t"))
                user_quantity_valid = True
            except ValueError:
                print("Enter a valid user quantity!")

        
        #Valid Quantity
        get_quantity_of_selected_item=inventory[stock_id][3]#stores fourth element of list
        while user_quantity<=0 or user_quantity>int(get_quantity_of_selected_item):#checks wheather input quantity is smaller than zero or greater than numbers of items present
            print("You are entering amount more than we have in stock")
            print("\n")
            user_quantity=int(input("Stock Quantity: \n"))

        #Update the text file
        new_inventory=clear_stock(stock_id,user_quantity)
        write.write_new_rent(new_inventory)
        
        """with open("item.txt","w") as file:
            for values in new_inventory.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                file.write("\n")"""
        exiter1=input("Press Enter to buy more, n to exit: ")
        if exiter1 =="n":
            exiter=False
            days_valid = False
            while days_valid == False:
                try:
                    days=int(input("For how many days you want to rent item"))
                    days_valid = True
                except ValueError:
                    print("Enter a valid day!")
    

         #getting user purchased items
    
        product_name= inventory[stock_id][0]
        selected_quantity=user_quantity
        unit_price= inventory[stock_id][2]
        selected_item_price= inventory[stock_id][2].replace("$","")
        total_price_of_selected_items= int(selected_item_price)*int(selected_quantity)
        dict_for_user_bought_product.append([product_name, selected_quantity, unit_price, total_price_of_selected_items])

        total=0
        for i in dict_for_user_bought_product:
            total+=int(i[3])
        grand_total=total
        today_date_and_time=datetime.now()
    print('\t \t \t \t BILL')
    print(" Babaji CENTER\n")
    print(" SHARINGAN |98XXXXXXX\n\n")
    print('---------------------------------------------------------------------------------')
    print("BILLS: " + unique_id )
    print("---------------------------------------------------------------------------------")
    print('Name of the customer: '+ str(name))
    print('Contact Number: '+ str(phoneNumber))
    print('Date and Time of Transaction: '+ str(today_date_and_time))
    print('---------------------------------------------------------------------------------')
    print('\n')
    print("Purchase detail are: ")
    print('--------------------------------------------------------------------------------------------------')
    print("Item Name \t\t\t Total Quantity \t\t Unit Price \t\t Total")
    print('--------------------------------------------------------------------------------------------------')
    for i in dict_for_user_bought_product:
        print(i[0], '\t',i[1],'\t',i[2],'\t','$',i[3])
    print('--------------------------------------------------------------------------------------------------')
    print('Grand Total: $\t\t\t' + str(grand_total))
    with open(name+str(phoneNumber)+".txt","w") as file:
        file.write('\t \t \t \t BILL')
        file.write(" Babaji CENTER\n")
        file.write(" SHARINGAN |98XXXXXXX\n\n")
        file.write('---------------------------------------------------------------------------------')
        file.write("BILLS: " + unique_id )
        file.write("---------------------------------------------------------------------------------")
        file.write('Name of the customer: '+ str(name))
        file.write('Contact Number: '+ str(phoneNumber))
        file.write('Date and Time of Transaction: '+ str(today_date_and_time))
        file.write('---------------------------------------------------------------------------------')
        file.write('\n')
        file.write("Purchase detail are: ")
        file.write('--------------------------------------------------------------------------------------------------')
        file.write("Item Name \t\t\t Total Quantity \t\t Unit Price \t\t Total")
        file.write('--------------------------------------------------------------------------------------------------')
        for i in dict_for_user_bought_product:
            file.write(str(i[0])+ '\t'+str(i[1])+'\t'+str(i[2])+'\t'+'$'+str(i[3]))
        file.write('--------------------------------------------------------------------------------------------------')
        file.write('Grand Total: $\t\t\t' + str(grand_total))
        
    







#Rental Return
def rental_return(inventory):



    name=input("Customer's Name: ")
    phone_number= input("Phone number: ")
    print("-------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------")
    print("S.N. \t\t item Name      Company Name     Price\t     Quantity")
    print("--------------------------------------------------------------------------------------------------")
    lines_of_inventories=read.read_items_line('item.txt')
    i=1
    for table_line in lines_of_inventories:
        
        print(i,"\t\t"+table_line.replace(',','\t'))
        i=i+1
    print('---------------------------------------------------------------------------------------------------')
    print("\n")
    #stock_id=int(input("Stock ID for rental return:"))
    
    dict_for_rental_return = []
    
    sys_exit = True
    while sys_exit == True:    
        stock_id=int(input("Stock ID Number:"))
        while stock_id<=0 or stock_id> len(inventory):
        
            print("Enter a valid stock ID!!!!!!!\t")
            #stock_id=int(input("Stock ID Number: "))
        user_quantity=int(input("Stock Quantity: "))

        
        #Valid Quantity
        get_quantity_of_selected_item=inventory[stock_id][3]#stores fourth element of list
        
        
        #checks wheather input quantity is smaller than zero or greater than numbers of items present
        while user_quantity<=0 or user_quantity>int(get_quantity_of_selected_item):
            print("Enter values from 1 to 5")
            user_quantity=int(input("Number of Stock: \n"))

        #Update the text file
        new_inventory=add_stock(stock_id,user_quantity)
        write.write_new_rent(new_inventory)
        
        
        exiter1=input("Enter n to exit: ")
        if exiter1 =="n":
            sys_exit=False
        
    

         #getting user purchased items
        unique_id = name + phone_number+"_Return"
        product_name= inventory[stock_id][0]
        selected_quantity=user_quantity
        unit_price= inventory[stock_id][2]
        selected_item_price= inventory[stock_id][2].replace("$","")
        total_price_of_selected_items= int(selected_item_price)*int(selected_quantity)
        dict_for_rental_return.append([product_name, selected_quantity, unit_price, total_price_of_selected_items])


    days = int(input("For how many days the item was booked: "))
    return_days=int(input("For how many days was the item kept: "))

    total=0
    fine_amount = 5
    delay = return_days / days
    rounded_value = int(delay + 0.999999)
    
    if rounded_value > 0:
        fine = (rounded_value - 1) * fine_amount

        dict_for_rental_return = {} # define dict_for_rental_return
        total_fine = 0 # initialize total_fine
    for i in dict_for_rental_return:
        total += int(i[3])
        total_fine += int(i[3])
            
            
            #total+=int(i[3]) 
            #total_fine +=int(i[3])
            
            
    
    grand_fine = total_fine +fine
    grand_total=return_days* grand_fine
    today_date_and_time=datetime.now()
    
    print('\t \t \t \t BILL')
    print(" \t \t \t \tBabaji CENTER\n")
    print(" \t \t \t \tSHARINGAN |98XXXXXXX\n")
    print('---------------------------------------------------------------------------------')
    print("BILLS " + unique_id)
    print("---------------------------------------------------------------------------------")
    print('Name of the customer: '+ str(name))
    print('Contact Number: '+ str(phone_number))
    print('Date and Time of Transaction: '+ str(today_date_and_time))
    print('---------------------------------------------------------------------------------')
    print('\n')
    print("Purchase detail are: ")
    print('--------------------------------------------------------------------------------------------------')
    print("Item Name \t\t\t Total Quantity \t\t Unit Price \t\t Total")
    print('--------------------------------------------------------------------------------------------------')
    for i in dict_for_rental_return:
        print(i[0], '\t',i[1],'\t',i[2],'\t','$',i[3])
    print('--------------------------------------------------------------------------------------------------')
    print("Total days Rented:  " + "\t\t\t\t\t\t"+ str(return_days) )
    print('--------------------------------------------------------------------------------------------------')
    print("Fine per unit for late return: "+ "\t\t\t\t\t\t"+ str(grand_fine))
    print('--------------------------------------------------------------------------------------------------')
    print('Grand Total: $\t\t\t\t\t\t' + str(grand_total))
    print('--------------------------------------------------------------------------------------------------')


