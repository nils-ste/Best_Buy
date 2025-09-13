import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(store_object):
    """Sets up the interface for the end user"""
    while True:
        user_input = input(f"Store Menu"
                           f"\n----------"
                           f"\n1. List all products in store "
                           f"\n2. Show total amount in store"
                           f"\n3. Make an order"
                           f"\n4. Quit"
                           f"\n\nPlease enter your choice: \n")

        if user_input == "1":
            counter = 1
            for product in store_object.get_all_products():
                print(f"{counter}. {product.show()}")
                counter += 1
            next_iteration = input(f"\nPlease press a button to continue... \n")

        if user_input == "2":
            store_object.get_total_quantity()

        if user_input == "3":
            print("-----")
            counter = 1
            choices = []
            for product in store_object.get_all_products():
                print(f"{counter}. {product.show()}")
                choices.append(product)
                counter += 1
            print("-----")
            order_list = []
            while True:
                order_decision = input(f"\nWhen you want to finish order, enter empty text."
                                       f"\nWhich product # do you want?")
                try:
                    if order_decision != "":
                        order_amount = int(input(f"\nPlease enter order amount:"))
                        order_list.append((choices[int(order_decision) - 1], order_amount))

                    """elif int(order_decision)-1 > len(order):
                        print("\nInvalid input. Please enter valid product #.")"""

                    if order_decision == "" and len(order_list) != 0:
                        print(f"******\n"
                              f"Order made! Total payment: ${best_buy.order(order_list)}")
                        break

                    if order_decision == "" and len(order) == 0:
                        print("******\n"
                              "No order placed.")
                except ValueError:
                    print("\nInvalid input. Please enter valid product #.")

        if user_input == "4":
            break


def main():
    start(best_buy)


if __name__ == "__main__":
    main()
