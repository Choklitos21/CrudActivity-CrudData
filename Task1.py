namesList = ["diego", "alfredo", "harry", "ben", "ash"]

flag = True
while flag:
    option = str(input("""
        Choose one option
        1. Add a new name that is not already on the list
        2. Show all names
        3. Update an existing name for a new one
        4. Remove a name by his position
        5. EXIT
        Enter your option from 1 to 5: """))
    match option:
        case "1":
            newName = str(input("Enter the new name: ")).strip().lower()
            if newName not in namesList:
                namesList.append(newName)
            else:
                print("That name is already on the list, use a new one\n")
        case "2":
            print("Names on the list\n")
            for i in namesList:
                print(f"* {i.capitalize()}")
        case "3":
            findName = str(input("Enter the new name you want to update: ")).strip().lower()
            if findName not in namesList:
                print("That name is not on the list, try another one\n")
            else:
                for i, name in enumerate(namesList):
                    if name == findName:
                        newName = str(input("Enter the new name: ")).strip().lower()
                        if newName not in namesList:
                            print(f"Old name {namesList[i].capitalize()} was updated for new name {newName.capitalize()}")
                            namesList[i] = newName
                        else:
                            print("That name is already on the list\n")
        case "4":
            option = input("Choose a position to remove from the list: ")
            if option.isalpha():
                print("Option no valid, use only numbers\n")
            elif 0 <= int(option) <= len(namesList):
                removed = namesList.pop(int(option))
                print(f"Name removed was {removed.capitalize()}")
            else:
                print("Option outside values, do not use less than 0 or more than amount of names on the list\n")
        case "5":
            print("\nProgram finished")
            flag = False
        case _:
            print("Option not valid, use only numbers from 1 to 5\n")
