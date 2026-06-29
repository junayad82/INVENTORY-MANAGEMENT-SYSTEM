inventory = []

while True:
    print("====INVENTORY MANGEMENT SYSTEM====")
    print("1. Add product")
    print("2. View product")
    print("3. Search product")
    print("4. Update stock")
    print("5. Sell product")
    print("6. Delete product")
    print("7. Show low stock products")
    print("8. Total inventory value")
    print("9. Exit")

    choice = input("Enter your choice: ")

    # Add product

    if choice == "1":
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter proucut stock: "))

        product = {
            "name": name,
            "price": price,
            "stock": stock,
            "available": True
        }

        inventory.append(product)

        with open("inventory.txt", "a") as file:
            file.write(f"Product name: {product['name']} | Price: {product['price']} | Stock: {product['stock']} | Available\n")

            print("Product add successfully!")

    # View product

    elif choice == "2":
        if len(inventory) == 0:
            print(" Sorry no product available😓")
        else:
            print("\nProduct List:")
            for i, product in enumerate(inventory, start=1):
                status = "Available" if product["available"] else "Sell"
                print(
                    f"{i}.{product['name']} | "
                    f"Price: {product['price']} | "
                    f"In stock: {product['stock']} | "
                    f"Status: {status}"
                )
                
    # Serach product

    elif choice == "3":

        search_product = input("Enter product name: ")
        found = False

        for product in inventory:
            if search_product.lower() == product["name"].lower():
                status = "Available" if product["available"] else "Unvailable"
                print(f"Ptoduct name: {product['name']}")
                print(f"Price: {product['price']}")
                print(f"Stock: {product['stock']}")
                print(f"Status: {status}")
                found = True
                break
        if not found:
            print("No product founded")

    # Update Stock

    elif choice == "4":
        name = input("Enter product name: ")

        found = False

        for product in inventory:
            if name.lower() == product["name"].lower():
                sotock_product = int(input("Enter product new stock: "))
                product["stock"] = sotock_product
                print("Product update successfully!")
                found = True
                break
        if not found:
            print("No product founded!")

    # Sell product

    elif choice == "5":
        sell_product = input("Enter sell product name: ")
        found = False
        for product in inventory:
            if sell_product.lower() == product["name"].lower():
                found = True
                if product["stock"] > 0:
                    product["stock"] -= 1
                    print("Product sold successfully!")   
                    if product["stock"] == 0:
                        product["available"] = False
                            
                else:
                    print("Out of stock!")
                    break
        if not found:
            print("No product founded!")

    # Delete product

    elif choice == "6":
        delete_product = input("Enter produt name to delete: ")
        found = False

        for product in inventory:
            if delete_product.lower() == product["name"].lower():
                inventory.remove(product)
                print("Product Delete successfully!")
                found = True
                break
        if not found:
            print("No product founded")

    # Show low stock product

    elif choice == "7":
        if len(inventory) == 0:
            print("No product founded!")
        else:
            print("\nLow stock product:")
            found = False

            for product in inventory:
                if product["stock"] <= 5:
                    print(
                        f"Product name: {product['name']} | "
                        f"Product price: {product['price']} | "
                        f"Product stock: {product['stock']} "
                    )   
                found = True
        if not found:
            print("No low stock founded!")

    
    # Total inventory value

    elif choice == "8":
        total = 0

        for product in inventory:

            total += product["price"] * product["stock"]

        print(f"\nTotal Inventory value: {total}")
    # Exit
    elif choice == "9":
        print("Good bye")
        break
    else:
        print("Invalide choice")


    








