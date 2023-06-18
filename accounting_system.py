balance = 0.0
warehouse = {}
operations = []
commands = ["balance", "sale", "purchase", "account", "list", "warehouse", "review", "end"]

while True:
    print("Available commands: ")
    print("-balance")
    print("-sale")
    print("-purchase")
    print("-account")
    print("-list")
    print("-warehouse")
    print("-review")
    print("-end")

    input_command = input("Enter the command: ")

    if input_command not in commands:
        print("Error command!Please input VALID command!")
    elif input_command == "balance":
        while True:
            add_or_subtract = input("Add or Subtract or Back:")
            if add_or_subtract == "add" or add_or_subtract == "Add":
                while True:
                    amount = input("Enter the amount you want to add (0 for back): ")
                    if amount == '0':
                        break
                    elif amount.replace(".", "").isnumeric():
                        amount = float(amount)
                        balance += amount
                        print(f"Added {amount} to account. Balance - {balance}")
                        operations.append(f"Added {amount} to account. Balance - {balance}")
                    else:
                        print("Please enter a VALID number!")
            elif add_or_subtract == "subtract" or add_or_subtract == "Subtract":
                while True:
                    amount = input("Enter the amount you want to subtract (0 for back): ")
                    if amount == '0':
                        break
                    elif amount.replace(".", "").isnumeric():
                        amount = float(amount)
                        if balance - amount < 0:
                            print(f"Error: Insufficient balance! Balance - {balance}")
                        else:
                            balance -= amount
                            print(f"Subtract {amount} to account. Balance - {balance}")
                            operations.append(f"Subtract {amount} to account. Balance - {balance}")
                    else:
                        print("Please enter a VALID number or enter 0 for back!")
            elif add_or_subtract == "back" or add_or_subtract == "Back":
                break
            else:
                print("Please enter the correct commands - Add or Subtract or Back!")
    elif input_command == "sale":
        product_name = input("Enter the name of the product: ")
        product_price = float(input("Enter the price of the product: "))
        product_quantity = int(input("Enter the quantity of the product: "))

        if product_name in warehouse and warehouse[product_name]['quantity'] >= product_quantity:
            total_sales_price = product_price * product_quantity
            balance += total_sales_price
            warehouse[product_name]['quantity'] -= product_quantity
            print(f"Successful sales {product_quantity} of {product_name} with {total_sales_price}. Balance - {balance}")
            operations.append(f"Sold {product_quantity} of {product_name} with {total_sales_price}. Balance - {balance}")
        elif product_name not in warehouse:
            print(f"Sales error: {product_name} not available in warehouse.")
        else:
            print("Sales error: Not enough quantity.")
    elif input_command == "purchase":
        product_name = input("Enter the name of the product: ")
        product_price = float(input("Enter the price of the product: "))
        product_quantity = int(input("Enter the quantity of the product: "))

        total_price = product_price * product_quantity

        if product_name in warehouse and warehouse[product_name]['price'] != product_price and warehouse[product_name]['quantity'] > 0:
            print(f"Purchase error: {product_name} already exists with different prices and quantities")
        else:
            if balance - total_price < 0:
                print("Purchase error: Insufficient balance!")
            else:
                balance -= total_price

            if product_name in warehouse:
                if warehouse[product_name]['price'] == product_price:
                    warehouse[product_name]['quantity'] += product_quantity
                elif warehouse[product_name]['quantity'] == 0:
                    warehouse[product_name].update({"price": product_price, "quantity": product_quantity})
            elif product_name not in warehouse:
                warehouse[product_name] = {"price": product_price, "quantity": product_quantity}

            print(f"Successful purchase {product_quantity} of {product_name} with {total_price}")
            operations.append(f"Purchased {product_quantity} of {product_name} with {total_price}. Balance - {balance}")
    elif input_command == "account":
        print(f"The current account balance: {balance}")
        operations.append(f"Checking the account balance. Balance - {balance}")
    elif input_command == "list":
        print("Total inventory in the warehouse: ")
        for name, value in warehouse.items():
            print(f"{name} - {value}")
        operations.append("Checking the total inventory in the warehouse")
    elif input_command == "warehouse": 
        product_name = input("Enter a product name: ")

        if product_name in warehouse:
            print(f"Status of {product_name} in the warehouse:")
            for k, v in warehouse[product_name].items():
                print(f"{k}: {v}")
            operations.append(f"Checking the status of {product_name} in the warehouse")
        else:
            print(f"{product_name} not available in warehouse")
    elif input_command == "review":
        from_indices = input("Enter 'From' index (Empty for the beginning): ")
        to_indices = input("Enter 'To' index (Empty for the beginning): ")

        if from_indices == "":
            from_indices = 0
        else:
            from_indices = int(from_indices)

        if to_indices == "":
            to_indices = len(operations)
        else:
            to_indices = int(to_indices)

        if from_indices < 0 or from_indices > to_indices or to_indices > len(operations):
            print(f"Error: Invalid range! Please emter between From: 0; To: {len(operations)}")
        else:
            print(f"Recorder operations (From {from_indices} to {to_indices}): ")
            for review in range(from_indices, to_indices):
                print(operations[review])
    elif input_command == "end":
        print("See you next time. Bye")
        break
