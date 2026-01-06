import pyttsx3
import time

engine = pyttsx3.init()

#Segregating the vending machine items into categories, putting them in separate dictionaries with each their own price and how much of that item is in stock.
snacks = { "A1": {"name": "Chips", "price": 3.50, "stock": 5},
    "A2": {"name": "Candy", "price": 2.50, "stock": 8},
    "A3": {"name": "Biscuits", "price": 2.00, "stock": 6},
    "A4": {"name": "Chocolate bar", "price": 2.25, "stock": 7},
    "A5": {"name": "Popcorn", "price": 4.00, "stock": 4},
    "A6": {"name": "Protein bar", "price": 5.25, "stock": 3}, }



cold_beverages = { "B1": {"name": "Soda", "price": 2.50, "stock": 10},
    "B2": {"name": "Water", "price": 1.00, "stock": 12},
    "B3": {"name": "Energy drink", "price": 4.50, "stock": 5},
    "B4": {"name": "Ice tea", "price": 3.00, "stock": 6},
    "B5": {"name": "Diet soda", "price": 2.50, "stock": 8}, }


hot_drinks = { "C1": {"name": "Hot-Chocolate", "price": 5.00, "stock": 4},
    "C2": {"name": "Coffee", "price": 3.00, "stock": 8},
    "C3": {"name": "Tea", "price": 2.00, "stock": 10},
    "C4": {"name": "Latte", "price": 4.00, "stock": 6},
    "C5": {"name": "Cappuccino", "price": 5.25, "stock": 5}, }


all_items = {**snacks, **cold_beverages, **hot_drinks} #Putting every category into one variable.


#Creating a new function/variable that will display the menu.
def menu():
    print("\n\n        || ~~~   VENDING MACHINE ~~~   ||\n")
    print("=======================================================")#User-friendly design.

    print("\nSNACKS\n")
    for i in snacks:
        item = snacks[i] #Searches the 'snacks' dictionary for snack code using a for loop.
        if item['stock'] > 0: #Check whether that item's 'stock' value is greater than 0; or if that item is still in stock.
            print(f"{i}: {item['name']:<25} AED{item['price']:.2f}  ({item['stock']} in stock.)") #:<25 formats the price and stock to left-aligned
            # to 25 chars,.2f formats the price with 2 decimals.
        else:
            print(f"{i}: {item['name']:<25} AED{item['price']:.2f}  (OUT OF STOCK)")#If the item is out of stock.

    print("\nCOLD BEVERAGES\n")
    for i in cold_beverages:
        item = cold_beverages[i]
        if item['stock'] > 0:
            print(f"{i}: {item['name']:<25} AED{item['price']:.2f}  ({item['stock']} in stock.)")
        else:
            print(f"{i}: {item['name']:<25} AED{item['price']:.2f}  (OUT OF STOCK)")

    print("\nHOT DRINKS\n")
    for i in hot_drinks:
        item = hot_drinks[i]
        if item['stock'] > 0:
            print(f"{i}: {item['name']:<25} AED{item['price']:.2f}  ({item['stock']} in stock.)")
        else:
            print(f"{i}: {item['name']:<25} AED{item['price']:.2f}  (OUT OF STOCK)")



# starting the program.
print("Starting vending machine...")
engine.say("Welcome to the vending machine!")
engine.runAndWait() #Line 67 and 68 runs the text-to-speech to say the phrase.

while True:
    menu()
    engine.say("Please select your item")
    engine.runAndWait() #The programs main loop (while loop) that will continually run until user chooses to quit the program/vending machine.


    code = input("\nEnter item code your item code (or input 'Q' to quit): ")
    code = code.upper() #Asks user to input an item code, then converts input to uppercase.


    if code == "Q":
        print("Thank you for your time!")
        engine.say("Thank you for your time!")
        engine.runAndWait()
        break #If the user doesn't want to use the vending machine, break the loop and end the code.


    if code not in all_items:
        print("Invalid code!")
        engine.say("Invalid code!")
        engine.runAndWait()
        continue #Displayed when user inputs an invalid code not in the vending machine, allows them to try again
        #with the continue function.

    # check stock
    if all_items[code]['stock'] <= 0:
        print(f"Sorry, {all_items[code]['name']} is out of stock!Please check out our other items.")
        engine.say(f"Sorry, {all_items[code]['name']} is out of stock!Please check out our other items.")
        engine.runAndWait()
        continue

    # show what they picked
    print(f"\nYou selected {all_items[code]['name']}.\n")
    engine.say(f"You selected {all_items[code]['name']}")
    engine.runAndWait()

    # get the price
    price = all_items[code]['price']
    print(f"Price: AED{price:.2f}")
    engine.say(f"Price is {price:.2f}")
    engine.runAndWait()

    # payment loop
    paid = False
    while paid == False:
        try:
            money = float(input("Insert money: $"))
            if money < price:
                need = price - money
                print(f"Not enough! Need AED{need:.2f} more.")
                engine.say(f"Not enough! Need {need:.2f} more.")
                engine.runAndWait()
            else:
                paid = True
                change = money - price
        except:
            print("Invalid amount!")
            engine.say("Invalid amount!")
            engine.runAndWait()

    # dispense the item
    print("")
    print("=======================================================")
    print(f"Dispensing {all_items[code]['name']}...")
    engine.say(f"Dispensing {all_items[code]['name']}")
    engine.runAndWait()

    print("\nPlease wait a moment...")
    for i in range(3, 0, -1):
        print(f"{i}..")
        time.sleep(1)

    print("Item dispensed!")
    engine.say("Item dispensed!")
    engine.runAndWait()
    print("=======================================================") #counts down from 3 till 0 to replicate a real
    #vending machine where customer waits for their item to be dispensed.



    all_items[code]['stock'] = all_items[code]['stock'] - 1 #Reduces the stock of the selected item (e.g. A chips packet)
    #by 1 when an item is dispensed.

    # give change
    if change > 0:
        print(f"\nYour change is: AED{change:.2f}")
        engine.say(f"Your change is {change:.2f}")
        engine.runAndWait()
    else:
        print("\nNo change.")
        engine.say("No change.")
        engine.runAndWait()

    #New variable 'suggestions',that holds a dictionary that will suggest items based on what they bought.
    suggestions = {"A5":"B1", #Popcorn : Soda
        "A1":"B1", #Chips : Soda
        "B5": "A6", #Diet soda : protein bar
        "C2": "A3",  #Coffee : Biscuits
        "C3": "A3",  #Tea : Biscuits
        "C4": "A4",  #Latte : Chocolate bar
        "C5": "A4",  #Cappuccino : Chocolate bar
    }
    # Check if the users chosen item code has a suggestion.
    if code in suggestions:
        suggested_code = suggestions[code]
        suggested_item = all_items[suggested_code]
        item = all_items[code]

        if suggested_item['stock'] > 0:
            print(f"\nWould you like a {suggested_item['name']} to go with your {item['name']}? Item code: {suggested_code}")
            engine.say( f"Would you like a {suggested_item['name']} to go with your {item['name']}? Item code: {suggested_code}")
            engine.runAndWait()

    #Asks the user if they want to purchase anything else.
    print("\n=======================================================")
    engine.say("Would you like to purchase another item?")
    engine.runAndWait()
    purchase_2 = input("Would you like to purchase another item?(Yes/No): ")
    if purchase_2.upper() == "NO":
        print("Thank you for your purchase!Goodbye!")
        engine.say("Thank you for your purchase!Goodbye!")
        engine.runAndWait()
        break






























