# This is the functionality that main is using
# The program will terminate if an error comes up while trying to search for an object within the db
# usually, for reasons of a bad connection. If it is a bad connection the db client will time out after 1000 milisecs,
import coffee
import connectDB
import re
import os.path
from os import path
import json




#### choice 1 ####
def addCoffeeItem():
    print("Adding a coffee item")
    while True:
        print("Please enter the coffee ID")
        itemId = input(">>>")

        # checking if integer
        if not re.match("^[0-9]*$",itemId):
            print("Sorry coffee id must be a number")

        # check if item id already exist
        elif searchCoffee(itemId) != "Sorry, but that item number isn't in our records":
                print("Sorry, but that coffee ID already exist")
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

        # Only except L, M, D
        if roasting != "L" and roasting != "M" and roasting != "D":
            print("Sorry, please choose L, M, or D ")
        else:
            break
    while True:
        print("Please enter the number of units avalible")
        quantity = input(">>>")

        # Check if integer
        if not re.match("^[0-9]*$", quantity):
            print("Sorry, the quantity must be a number")
        else:
            break
    # This is my class object
    newCoffee = coffee.Coffee(itemId,name, pricePerLB, roasting, quantity)
    print(newCoffee)

    # Json object to insert into db
    coffeeObject = {
        "itemId" : int(itemId),
        "name" : str(name),
        "pricePerLB" : int(pricePerLB),
        "roasting" : str(roasting),
        "quantity" : int(quantity)
    }
    try:
        connectDB.collection.insert_one(coffeeObject)
    except BaseException as e:
        print(e)


#### choice 2 #### 
def searchCoffee(id=''):
    results = ''
    if id =='':
        while True:
            print("Enter the coffee's item number")
            # I made this global so that I can search the itemId before enacting any CRUD operation 
            global coffeeId
            coffeeId = input(">>>")
            if not re.match("^[0-9]*$", coffeeId):
                print("Sorry, please enter a number")
            else:
                break
    
        coffeeId = int(coffeeId)
        try:
            results = connectDB.collection.find_one({"itemId" : coffeeId})
            results = str(results)
        except BaseException:
            print("Sorry, something went wrong")
            print("Terminating program...")
            quit()
    else:
        id = int(id)
        try:
            results = connectDB.collection.find_one({"itemId" : id})
            results = str(results)
        except BaseException:
            print("Sorry, something went wrong")
            print("Terminating program...")
            quit()
            
    if results == "None":
        return "Sorry, but that item number isn't in our records"
    else:
        return results


#### choice 3 ####
def deleteCoffee():
    results = searchCoffee()
    if results != "Sorry, but that item number isn't in our records":
        print(results)
        print("Do you want to delete this coffee item?\ny) yes\nn) no")
        choice = input(">>>")

        # Verify that they want to delete item. 
        # This will exit the deleting process if any value other than y/Y is selected
        if choice == 'y' or choice == 'Y':
            connectDB.collection.delete_one({"itemId" : coffeeId})  
            print("Item has deleted")
        else:
            print("Deleting process was canceled...")
    else:
        print(results)

#### choice 4 ####
def updateCoffee():
    results = searchCoffee()
    if results != "Sorry, but that item number isn't in our records":
        print(results)
        print("Do you want to update this coffee item\ny) yes\nn) no")
        choice = input(">>>")

        # Verify that they want to update item. 
        # This will exit the upgrading process if any value other than y/Y is selected
        if choice == 'y' or choice =='Y':
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
                        print(searchCoffee(coffeeId))

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
                        print(searchCoffee(coffeeId))
                        break
            else:
                print("Invalid option")            
        else:
            print("Updating process was canceled...")
    else:
        print(results)

#### choice 5 ####
def importJson():
    print("Please enter the name of json file. ex: myFile.json")
    file = input(">>>")
    # Checking if the file exists
    if path.exists(file):
        file = open(file, 'r')
        jsonFile = json.load(file)

        for item in jsonFile['coffee']:
            # Don't add ones that are already stored in the db
            if searchCoffee(item['itemId']) == "Sorry, but that item number isn't in our records":
                newCoffee = coffee.Coffee(item['itemId'],item['name'],item['pricePerLB'],item['roasting'], item['quantity'])
                print(newCoffee)
                print("\n")
                try:
                    connectDB.collection.insert_one(item)
                except BaseException as e:
                    print(e)       
        print("Importing was successful!")
        file.close()
    else:
       print("Sorry, file not found")

#### choice 6 ####
def exportJson():
    print("Exporting file...")

    file = open("coffeeExport.json", 'w')
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