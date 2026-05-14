# Variables
products = []
option = []

# Method main 
while option != "5": 
    print("1. Add product")
    print("2. Remove product")
    print("3. View products")
    print("4. Update product")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        # Name validation
        name = input("Enter product name: ")

        while name == "":
            print("Product name cannot be empty. Please try again.")
            name = input("Enter product name: ")

        # Category validation
        category = input("Enter product category: ")

        while category == "":
            print("Product category cannot be empty. Please try again.")
            category = input("Enter product category: ")

        # Price validation
        price = input("Enter product price: ")

        while price == "" or not price.isdigit():
            print("Product price must be a valid number. Please try again.")
            price = input("Enter product price: ")

        # Convert price to integer
        price = int(price)

        products.append([name, category, price])

        print("Product added successfully!")

    elif option == "2":
        name = input("Enter product name to remove: ")
        products = [product for product in products if product[0] != name]
        print("Product removed successfully!")

    elif option == "3":
        if not products:
            print("No products available.")
        else:
            for product in products:
                print(f"Name: {product[0]}, Category: {product[1]}, Price: {product[2]}")

    elif option == "4":
        name = input("Enter product name to update: ")
        for product in products:
            if product[0] == name:
                new_price = input("Enter new price: ")
                while new_price == "" or not new_price.isdigit():
                    print("Product price must be a valid number. Please try again.")
                    new_price = input("Enter new price: ")
                new_price = int(new_price)
                product[2] = new_price
                print("Product updated successfully!")
                break
        else:
            print("Product not found.")

    elif option == "5":
        print("Exiting the program. Goodbye!")

    else:
        print("Invalid option. Please try again.")
    