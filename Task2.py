products = {
    "cafe": 10.50,
    "leche": 5.99,
    "huevos": 6.00,
    "pan": 4.99
}

flag = True
while flag:
    option = str(input("""
        Choose one option
        1. Add new product with his price
        2. Search for an existing product
        3. Update price for an existing product
        4. Remove a product from inventory
        5. EXIT
        Enter your option from 1 to 5: """))
    match option:
        case "1":
            newProductName = str(input("What's the new product name?: ")).strip().lower()
            newProductPrice = input("What's the new product price?: ").strip()
            if newProductName in products:
                print("That product already exists")
            elif newProductPrice.isalpha():
                print("Price invalid, use only numbers")
            elif float(newProductPrice) < 0:
                print("Price cannot be less than 0")
            else:
                products[newProductName] = float(newProductPrice)
                print("Product added correctly")
                print(products)
        case "2":
            productName = str(input("Enter the product name to search: "))
            if products.get(productName) is not None:
                print(f"The product {productName.capitalize()} exists")
                print(products)
            else:
                print(f"{productName.capitalize()} do not exists")
                print(products)
        case "3":
            productName = str(input("Enter the product name to update its price: "))
            productNewPrice = input("Enter the new price: ")
            if productName not in products:
                print("That product is not in the inventory")
            elif productNewPrice.isalpha():
                print("Price has to be only numbers")
            elif float(productNewPrice) < 0:
                print("Price cannot be less than 0")
                print("Price invalid, use only numbers")
            else:
                products[productName] = float(productNewPrice)
                print("Price updated")
                print(products)
        case "4":
            productName = str(input("Enter the product name to remove from the inventory: "))
            if productName not in products:
                print("That product is not in inventory")
            else:
                print(f"The product {productName.capitalize()} was removed from the inventory")
                products.pop(productName)
                print(products)
        case "5":
            print("\nProgram finished")
            flag = False
        case _:
            print("Option not valid, use only numbers from 1 to 5\n")