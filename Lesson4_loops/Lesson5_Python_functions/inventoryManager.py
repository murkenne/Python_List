# Exercise 5: The Product Inventory Manager

products = ['T-shirt', 'Jeans', 'Sneakers', 'Hat', 'Sunglasses', 'Jacket', 'Watch']

def manage_inventory():
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Remove Product")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("\nCurrent Inventory:")
            for product in products[:5]:
                print(product)
            if len(products) > 5:
                print('...and more')
        elif choice == '2':
            new_product = input("Enter the name of the new product: ")
            products.append(new_product)
            print(f"{new_product} has been added to the inventory")
        elif choice == '3':
            product_to_remove = input("Enter the name of the product to remove: ")
            if product_to_remove in products:
                product.remove(product_to_remove)
                print(f"{product_to_remove} has been removed from the inventory")
            else:
                print(f'{product_to_remove} was not found in the inventory.')
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
    
manage_inventory()