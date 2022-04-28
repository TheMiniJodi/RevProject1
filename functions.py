from debugpy import connect
import coffee
import re
import os.path
from os import path
import json
import connectDB



# choice #1
# TODO check to see if a coffee id exist before adding it
def addCoffeeItem():
    print("Adding a coffee item")
    while True:
        print("Please enter the coffee ID")
        itemId = input(">>>")

        # checking if integer
        if not re.match("^[0-9]*$",itemId):
            print("Sorry coffee id must be a number")
        else:
            break
    
    print("Please enter the name of the coffee")
    name= input(">>>")

    # Don't allow ',' in name
    if "," in name:
        name = re.sub(',',' ',name)

    while True:
        print("Please enter the price per pound")
        pricePerLB = input(">>>")

        # checking if integer
        if not re.match("^[0-9]*$", pricePerLB):
            print("Sorry, the price per pound must be a number")
        else:
            break

    while True:
        print("Please enter the roasting type ex: L, M, D")
        roasting = input(">>>")
        if roasting != "L" and roasting != "M" and roasting != "D":
            print("Sorry, please choose L, M, or D ")
        else:
            break
    while True:
        print("Please enter the number of units avalible")
        quantity = input(">>>")
        if not re.match("^[0-9]*$", quantity):
            print("Sorry, the quantity must be a number")
        else:
            break
    newCoffee = coffee.Coffee(itemId,name, pricePerLB, roasting, quantity)

    coffeeObject = {
        "itemId" : int(itemId),
        "name" : str(name),
        "pricePerLB" : int(pricePerLB),
        "roasting" : str(roasting),
        "quantity" : int(quantity)
    }
    connectDB.collection.insert_one(coffeeObject)
    print("Coffee item has been added")
    return newCoffee 


# choice #2
def searchCoffee():
    while True:
        print("Enter the coffee's item number")
        global coffeeId
        coffeeId = input(">>>")
        if not re.match("^[0-9]*$", coffeeId):
            print("Sorry, please enter a number")
        else:
            break
    
    coffeeId = int(coffeeId)
    results = connectDB.collection.find_one({"itemId" : coffeeId})
    results = str(results)
    if results == "None":
        return "Sorry, but that item number isn't in our records"
    else:
        return results
        

# choice #3
def deleteCoffee():
    print(searchCoffee())
    print("Do you want to delete this coffee item?\ny) yes\nn) no")
    choice = input(">>>")
    if choice == 'y' or choice == 'Y':
        connectDB.collection.delete_one({"itemId" : coffeeId})  
        print("Item has deleted")
    else:
        print("Deleting process was canceled...")

# choice #4
def updateCoffee():
    result = searchCoffee()
    if result != "Sorry, but that item number isn't in our records":
        print(result)
        print("Do you want to update this coffee item\ny) yes\nn) no")
        choice = input(">>>")

        if choice == 'y' or choice =='Y':
            # Update item
            print("Select which option you would like to update\n1) price per pound\n2) quantity")
            field = input(">>>")

            if field == "1":
                while True:
                    print("Please enter the new price per pound")
                    newPrice = input(">>>")
                    if not re.match("^[0-9]*$", newPrice):
                        print("Please enter a number")
                    else:
                        connectDB.collection.update_one({"itemId": coffeeId},{"$set":{"pricePerLB": int(newPrice)}})
                        print("Price per pound has been updated")
                        break
            elif field == "2":
                while True:
                    print("Please enter the new quantity")
                    newQuantity = input(">>>")
                    if not re.match("^[0-9]*$", newQuantity):
                        print("Please enter a number")
                    else:
                        connectDB.collection.update_one({"itemId": coffeeId},{"$set":{"quantity": int(newQuantity)}})
                        print("Quantity has been updated")
                        break
            else:
                print("Invalid option")            
        else:
            print("Updating process was canceled...")
    else:
        print("Sorry, but that item number isn't in our records")

# choice #5
def importJson():
    print("Please enter the name of json file. ex: myFile.json")
    file = input(">>>")
    if path.exists(file):
        file = open(file, 'r')
        jsonFile = json.load(file)

        for item in jsonFile['coffee']:
            connectDB.collection.insert_one(item)       
        print("Importing was successful!")
        file.close()
    else:
       print("Sorry, file not found")

# choice #6
def exportJson():
    print("Exporting file...")
    file = open("coffeeExport.json", 'w')
    temp ={}
    coffee = connectDB.collection.find()
    numItems = len(list(coffee))
    coffee=connectDB.collection.find()
    file.write('{"coffee":[')
    for item in coffee:
        temp={
            "itemId": item['itemId'],
            "name": item['name'],
            "pricePerLB" : item['pricePerLB'],
            "roasting": item['roasting'],
            "quantity": item['quantity']
            }
        json.dump(temp, file, indent=4)
        if numItems > 1:
            numItems -= 1
            file.write(',')
    file.write("]}")
    file.close()
    print("Export complete")
  
    
def main():
    # myCoffeeList =[]
    while True:
        print("----------------------------------\n"
            "       Coffee Inventory App       \n" 
            +"----------------------------------\n"
            + "1 Add coffee item\n"
            + "2 Search coffee products\n"
            + "3 Delete coffee item\n"
            + "4 Update coffee item\n" 
            + "5 Import Json file\n"
            + "6 Export Json file\n"
            + "q to quit")

        userInput = str(input(">>>"))
        
        if userInput == "1":
            # myCoffeeList.append(addCoffeeItem())
            print(addCoffeeItem())
        elif userInput == "2":
            print(searchCoffee())
        elif userInput == "3":
            deleteCoffee()
        elif userInput == "4":
            updateCoffee()
        elif userInput == "5":
            print("Import Json file")
            importJson()
        elif userInput == "6":
            exportJson()
        elif userInput == 'q' or userInput =='Q':
            quit()  
        else:
            print("Invaild Option")

    
    
main()