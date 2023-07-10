# import function to load and save data
import data_import as di

print("""Welcome to the Warehouse management system!
      Loading current balance, inventory, and operation history...""")

# Open files to load data
curr_balance = di.load_data("curr_balance.txt")
stock = di.load_data("stock.txt")
history = di.load_data("history.txt")

# Default account value
if curr_balance == " ":
    curr_balance = 0

if stock == " ":
    stock = {}

if history == " ":
    history = []

# Start while loop for the program launch
while True:
# Print list of command upon launching, display function of each command before each command prompt

    print("""
    Enter any of the following command to start:
    - 'balance': To make change on current balance
    - 'sale': To record a sale (Product name, price, quantity)
    - 'purchase': To record a purchase (Product name, price, quantity)
    - 'account': To check the current account balance.
    - 'list': To check the total inventory in the warehouse (Product name, price, quantity)
    - 'warehouse': To check a product name and its status in the warehouse.
    - 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range. 
    - 'end': To exit the program""")

# Ask user to input a command
    command = input("\nEnter command: ")
    
# Use if else statement for command selection
  # 'balance': The program should prompt for an amount to add or subtract from the account.
    if command == "balance":
        acc_change = float(input("Enter the amount to be added to the account balance, use negative number for subtraction: "))
        curr_balance += acc_change
        # Add record of change to history list
        change = "$" + str(acc_change) + " was added to the account. Current balance on the acc is $" + str(curr_balance) + "."
        history.append(change)

  # 'sale': The program should prompt for the name of the product, its price, and quantity. Perform necessary calculations and update the account and warehouse accordingly.
    elif command == "sale":
        # Prompt for product name, price, and quantity sold
        sname = input("Name of sold product: ")
        sprice = float(input("Price of sold product: "))
        squantity = int(input("Quantity sold: "))
        # Adjust quantity of product if the product is already listed
        if sname in stock:
            # Check if there is sufficient amount
            if stock[sname]["quantity"] >= squantity:
                stock[sname]["quantity"] -= squantity
                # Change account balance based on total sale price
                curr_balance += (sprice * squantity)
                # Add record of change to history list
                change = str(squantity) + " unit of " + sname + " was sold. $" + str(squantity * sprice) + " amount was earned."
                history.append(change)
            else:
                print(f"Insufficient quantity for sales. ")
        # Print message for user to know that the item is not in stock
        else:
            print(f"The item {sname} is not available.")
        

  # 'purchase': The program should prompt for the name of the product, its price, and quantity. Perform necessary calculations and update the account and warehouse accordingly. Ensure that the account balance is not negative after a purchase operation.
    elif command == "purchase":
        # Prompt for product name, price, and quantity purchased
        pname = input("Name of purchased product: ")
        pprice = float(input("Unit price of purchased product: "))
        pquantity = int(input("Quantity purchased: "))
        # Check if current balance is sufficient to make a purchase
        if (pprice * pquantity) > curr_balance:
            print("There's no sufficient balance to make the purchase.")
            continue

        # Adjust quantity of product if the product is already listed
        if pname in stock:
            stock[pname]["quantity"] += pquantity
            # Change account balance based on total sale price
            curr_balance -= (pprice * pquantity)    
        # Add record of new product if product not listed yet
        else:
            stock[pname] = {
              "unit_price": pprice,
              "quantity": pquantity
            }
        # Add record of change to history list
        change = str(pquantity) + " unit of " + pname + " was purchased. $" + str(pquantity * pprice) + " was spent."
        history.append(change)

  # 'account': Display the current account balance.
    elif command == "account":
        print(f"The current balance on the account is ${curr_balance}.")
  # 'list': Display the total inventory in the warehouse along with product prices and quantities.
    elif command == "list":
        # Print header
        print("Product name | Unit price |  Quantity")
        print("----------------------------------------")
        # Print content
        for product, info in stock.items():
            unit_price = info["unit_price"]
            quantity = info["quantity"]
            print(f"{product:<12} | {unit_price:>12} | {quantity:>12}")
  # 'warehouse': Prompt for a product name and display its status in the warehouse.
    elif command == "warehouse":
        search_name = input("Please enter a product name to search: ")
        if search_name in stock:
            quantity = stock[search_name]["quantity"]
            price = stock[search_name]["unit_price"]
            print(f""" Search result for {search_name}:
                  Quantity: {quantity}
                  Unit price: {unit_price}
                  """)
        else:
            print(f"{search_name} is not on the warehouse record.")
  # 'review': Prompt for two indices 'from' and 'to', and display all recorded operations within that range. If ‘from’ and ‘to’ are empty, display all recorded operations. Handle cases where 'from' and 'to' values are out of range.
    elif command == "review":
        n_hist = len(history)
        print(f"{n_hist} operation(s) recorded on history. Please enter a from and to value to filter the result.\n")
        # Prompt user to enter from and to value, print full list if no value entered
        start = input("Please enter a from value: ")
        end = input("Please enter a to value: ")

        if start == "" and end == "":
            # Print header
            print("++++++++++ Operation history ++++++++++")
            print("----------------------------------------")
            # Print each line of history using iteration
            for i in history:
                print(i)
        elif start == "" and end != "":
            end = int(end)
            filter_hist = history[:end]
            # Print header
            print("++++++++++ Operation history ++++++++++")
            print("----------------------------------------")
            # Print filtered history using iteration
            for i in filter_hist:
                print(i)
        elif start != "" and end == "":
            start = int(start)
            filter_hist = history[start-1:]
            # Print header
            print("++++++++++ Operation history ++++++++++")
            print("----------------------------------------")
            for i in filter_hist:
                print(i)            
        else:
            start = int(start)
            end = int(end)
            # Splice list based on range provided
            filter_hist = history[start-1:end]
            # Print header
            print("++++++++++ Operation history ++++++++++")
            print("----------------------------------------")
            for i in filter_hist:
                print(i)


  # 'end': Terminate the program.
    elif command == "end":
        print("Saving data to files...")
        # Save data into files
        di.write_data("curr_balance.txt", curr_balance)
        di.write_data("stock.txt", stock)
        di.write_data("history.txt", history)
        # Print goodbye message
        print("Data saved successfully. Ending program...Goodbye!")

        break
    else:
        print("Invalid command. Please enter another command.")