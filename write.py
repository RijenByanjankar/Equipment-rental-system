def write_new_rent(new_inventory):
    with open("item.txt","w") as file:
            for values in new_inventory.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3]))
                file.write("\n")
    with open("fasdfdsafds.txt", "w") as invoice:
         invoice.write("................")