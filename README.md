# Coffee Inventory Application
This is a CLI of an MVP of a coffee inventory application that a coffee shop would use to keep track of their coffee products. When the user starts the program it will present a menu with the options: add a coffee item, search coffee products, delete a coffee item, update coffee item, import a JSON file, export a JSON file, and quit. This is a recursive menu where the user must select the quit option to exit the program. The user will be able to add, search, update, and delete a coffee item by ID. When adding a coffee item, if the ID exists the program will prompt the user with a message stating that the ID already exists. The ID must be unique and not exist within the database to be added. For updating, searching, and deleting, if the ID doesn't exist in the database the program will prompt with a message that it doesn't exist. When the user chooses to import data via JSON file they will be prompted to enter a file name. The program will check if the file exists; if so it will import the data; if not it will prompt with a message stating that it does not exist. When exporting data the program will write to a new file of all the data stored in the database.

# Technologies Used


- Python3
- MongoDB
- VS Code
- Git/GitHub

# Features
- Data is stored and saved in MongoDB
- User can add as many coffee items as they want
- Search coffee products
- Delete a coffee item
- Update coffee item
- Import a JSON file
- Export data to JSON file

**To-do-list**
  - Add error handling around reading imported JSON files
    - wrong format
  - Show a count of how many coffee items were added on import
    - If zero items were added prompt with message saying no coffee items added
 
 # Getting Started
 
 **Pre Requirements**
  - Git CLI
  - Python3 
  - MongoDB connection


 **unix:**
 - git clone https://github.com/TheMiniJodi/RevProject1.git
 - python3 
 
    
 # Usage
 
 
 CLI interation:


<img width="467" alt="Screen Shot 2022-05-27 at 1 35 00 PM" src="https://user-images.githubusercontent.com/18232226/170770541-1d7c2417-f69a-4cc1-97a0-2f25f0155286.png">




