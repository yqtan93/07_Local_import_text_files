import data_import as di

class Manager:

    def __init__(self):
        self.actions = {}

    def assign(self, name):
        # method to assign tasks to appropriate operations in the accounting system
        def inner_function(func):
            self.actions[name] = func

        return inner_function
    
    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Command not defined. Please enter available command\n.")

        else:
            self.actions[name](*args, **kwargs)

if __name__ == "__main__":
    manager = Manager()

    @manager.assign("balance")
    def balance(curr_balance, history):
        acc_change = float(input("Enter the amount to be added to the account balance, use negative number for subtraction: "))
        curr_balance += acc_change
        # Add record of change to history list
        change = "$" + str(acc_change) + " was added to the account. Current balance on the acc is $" + str(curr_balance) + "."
        history.append(change)

    @manager.assign("account")
    def account(curr_balance):
        print(f"The current balance on the account is ${curr_balance}.")

    @manager.assign("sale")
    def sale(curr_balance, stock, history):
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

    @manager.assign("purchase")
    def purchase(curr_balance, stock, history):
        # Prompt for product name, price, and quantity purchased
        pname = input("Name of purchased product: ")
        pprice = float(input("Unit price of purchased product: "))
        pquantity = int(input("Quantity purchased: "))
        # Check if current balance is sufficient to make a purchase
        if (pprice * pquantity) > curr_balance:
            print("There's no sufficient balance to make the purchase.")

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

    @manager.assign("inventory")
    def inventory(stock):
        # Print header
        print("Product name | Unit price |  Quantity")
        print("----------------------------------------")
        # Print content
        for product, info in stock.items():
            unit_price = info["unit_price"]
            quantity = info["quantity"]
            print(f"{product:<12} | {unit_price:>12} | {quantity:>12}")

    @manager.assign("product")
    def product(stock):
        search_name = input("Please enter a product name to search: ")
        if search_name in stock:
            quantity = stock[search_name]["quantity"]
            unit_price = stock[search_name]["unit_price"]
            print(f""" Search result for {search_name}:
                Quantity: {quantity}
                Unit price: {unit_price}
                """)
        else:
            print(f"{search_name} is not on the warehouse record.")

    @manager.assign("review")
    def review(history):
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

    @manager.assign("end")
    def end(curr_balance, stock, history):
        print("Saving data to files...")
        # Save data into files
        di.write_data("curr_balance.txt", curr_balance)
        di.write_data("stock.txt", stock)
        di.write_data("history.txt", history)
        # Print goodbye message
        print("Data saved successfully. Ending program...Goodbye!")


