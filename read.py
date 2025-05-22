def read_items(itemlists):
    #with open, opens the file item.txt and 'r' read the file and store in variable 'file'
     with open(itemlists,'r') as file:
            #Creating an empty dictionary
            item_dictionary={} 
            item_id=1 
            #iterates every line in file
            for line_inFile in file: 
                #replacing empty line with spaces
                line_inFile=line_inFile.replace("\n",'') 
                #Using the comma as a seperator
                item_dictionary[item_id]=line_inFile.split(",") 
                item_id=item_id+1
            return item_dictionary


def read_items_line(itemlists):
    our_list=[]
    with open(itemlists,'r') as file:
        a=1


        for line in file:
            
            line
            our_list.append(line.rstrip())
            a=a+1
    return our_list

#print(len(read_items("item.txt")))


            
          
               