catalog = (10, 20, 30, 40, 50, 60)

flag = True
while flag:
    option = str(input("""
        Choose one option
        1. How would it look if a new value were added at the end
        2. How would it look if one value were replaced by a new one
        3. How would it look if a value were deleted from its position
        4. Show all values with their positions.
        5. Show: Highest, lowest, Total sum, Highest value position
        6. EXIT
        Enter your option from 1 to 6: """))
    match option:
        case "1":
            newNumber = input("Enter the new number to add: ")
            if newNumber.isalpha():
                print("Invalid, use only numbers")
            else:
                newTuple = catalog + (int(newNumber),)
                print(f"The tuple adding the new number would look like this: {newTuple}")
                print(newTuple)
        case "2":
            oldValue = input("Value to replace: ")
            newValue = input("New value: ")

            if oldValue.isalpha() or newValue.isalpha():
                print("Values have to be numbers, not letters")
            elif int(oldValue) not in catalog:
                print("That number is not on the catalog")
            else:
                index = catalog.index(int(oldValue))
                print(index)
                partOneTuple = catalog[:index]
                partTwoTuple = catalog[index + 1:]
                finalTuple = partOneTuple + (int(newValue), ) + partTwoTuple
                print(f"The new tuple would look like this {finalTuple}")
        case "3":
            print(f"Actual tuple: {catalog}")
            position = input("Value to remove: ")

            if position.isalpha():
                print("Value have to be a number, not letters")
            elif int(position) not in catalog:
                print("That number is not on the catalog")
            else:
                index = catalog.index(int(position))
                partOneTuple = catalog[:index]
                partTwoTuple = catalog[index + 1:]
                finalTuple = partOneTuple + partTwoTuple
                print(f"Value removed: {catalog[index]}")
                print(f"The new tuple would look like this {finalTuple}")
        case "4":
            for position, value in enumerate(catalog):
                print(f"Value: {value}, Position: {position}")
        case "5":
            print(f"""
        Highest: {max(catalog)}
        Lowest: {min(catalog)}
        Total sum: {sum(catalog)}
        Highest value {max(catalog)} in the position {catalog.index(max(catalog))}
        """)
        case "6":
            print("\nProgram finished")
            flag = False
        case _:
            print("Option not valid, use only numbers from 1 to 6\n")