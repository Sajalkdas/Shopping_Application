import pickle
import os.path
from Product import Product
from ShoppingCart import ShoppingCart
from MyStore import MyStore, add_product


def main():
    fname = 'ProductsData.txt'
    plist = []
    scart = ShoppingCart()  # Initialize scart to empty
    store = MyStore()
    plist = store.read_products_from_file(fname)

    # Check if pickle file exists
    pickle_file = 'shoppingcart_pickle.pkl'
    if os.path.isfile(pickle_file):
        # Load plist and scart from pickle file
        with open(pickle_file, 'rb') as f:
            plist = pickle.load(f)
            scart = pickle.load(f)

    main_menu = ('\n---Main Menu---' + '\n' + '1. View Products' + '\n' + '2: Shop' + '\n'
                 + '3: Checkout' + '\n' + '4: Add another product' + '\n' + '5: Remove a product' + '\n' + '0: Exit')
    shopping_menu = ('\n\t1: Add Product to Cart' + '\n\t' + '2: Remove Product From Cart'
                     + '\n\t' + '3: Show Cart' + '\n\t' + '4: Clear Cart' + '\n\t' + '0: back to main')
    menu_option = 1
    while menu_option > 0:
        print('\n'+main_menu)
        menu_option = input('Please enter an option: ')
        menu_option = int(menu_option)
        if menu_option == 0:
            # Save plist and scart to pickle file
            with open(pickle_file, 'wb') as file:
                pickle.dump(plist, file)
                pickle.dump(scart, file)
            print('Quitting Application..')
            break  # exit main loop
        if menu_option == 1:
            store.show_products()
        if menu_option == 2:
            shopping_menu_option = 1
            while shopping_menu_option > 0:
                print('\n'+shopping_menu)
                soption = input('\tPlease enter a shopping option: ')
                shopping_menu_option = int(soption)
                if shopping_menu_option == 1:  # add to cart
                    pid_qty = input('\tPlease enter [product_id,quantity]: ')
                    parts = pid_qty.split(',')
                    if len(parts) != 2:
                        print('Invalid input format. Please enter in the format [product_id,quantity].')
                        continue  # Go back to the shopping menu
                    pid = int(parts[0])
                    qty = int(parts[1])
                    pr = store.get_product(pid)
                    if pr is not None:
                        scart.add_item(pr, qty)
                if shopping_menu_option == 2:  # remove from cart
                    pid = input('Please enter product id to remove from cart: ')
                    scart.remove_item(int(pid))
                if shopping_menu_option == 3:  # view cart
                    scart.show_cart()
                if shopping_menu_option == 4:
                    scart.clear_cart()
        if menu_option == 3:  # checkout
            total = scart.compute_total()
            print(total)
            total_after_discount = scart.apply_discount(total)
            print('\n-----Check Out Info-----')
            print('Total Amount = ', total, ' Total Amount after discount=', total_after_discount)
        if menu_option == 4:
            data = input('Please Enter Product Data [product id,name,price,category]: ')
            parts = data.split(',')
            product = Product(int(parts[0]), parts[1], float(parts[2]), parts[3])
            add_product(fname, product)
            print("Product added successfully!")

        if menu_option == 5:
            pid = input('\t Please enter a product id to remove: ')
            removed = False
            for item in plist:
                if item.product_id == int(pid):
                    plist.remove(item)
                    removed = True
                    break
            if removed:
                store.remove_product(fname, plist)
                print("Product removed successfully!")
            else:
                print("Product not found!")


main()
