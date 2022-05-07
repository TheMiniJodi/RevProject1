# This is the functionality for the menu options. It will keep running until the user selects 'q' or 'Q'

import pprint
import functions

def main():
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
            functions.addCoffeeItem()
        elif userInput == "2":
            pprint.pprint(functions.searchCoffee())
        elif userInput == "3":
            functions.deleteCoffee()
        elif userInput == "4":
            functions.updateCoffee()
        elif userInput == "5":
            functions.importJson()
        elif userInput == "6":
            functions.exportJson()
        elif userInput == 'q' or userInput =='Q':
            quit()  
        else:
            print("Invaild Option")

    
if __name__ == '__main__':   
    main()