import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(store_object):
    """Sets up the interface for the end user."""
    while True:
        user_input = input(
            "Store Menu"
            "\n----------"
            "\n1. List all products in store "
            "\n2. Show total amount in store"
            "\n3. Make an order"
            "\n4. Quit"
            "\n\nPlease enter your choice: \n"
        )

        if user_input == "1":
            counter = 1
            for product in store_object.get_all_products():
                print(f"{counter}. {product.show()}")
                counter += 1
            input("\nPlease press a button to continue... \n")

        if user_input == "2":
            total = store_object.get_total_quantity()
            print(f"\nTotal quantity in store: {total}\n")

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
                order_decision = input(
                    "\nWhen you want to finish order, enter empty text."
                    "\nWhich product # do you want?"
                )
                try:
                    if order_decision != "":
                        index = int(order_decision) - 1
                        if index < 0 or index >= len(choices):
                            print("\nInvalid input. Please enter valid product #.")
                        else:
                            order_amount = int(input("\nPlease enter order amount:"))
                            order_list.append((choices[index], order_amount))

                    if order_decision == "" and len(order_list) != 0:
                        print(
                            "******\n"
                            f"Order made! Total payment: ${best_buy.order(order_list)}"
                        )
                        break

                    if order_decision == "" and len(order_list) == 0:
                        print("******\n"
                              "No order placed.")
                except ValueError:
                    print("\nInvalid input. Amount order surpasses the quantity in stock.")
                    order_list.remove(order_list[index])

        if user_input == "4":
            break


def main():
    """Entry point for the CLI application."""
    start(best_buy)


if __name__ == "__main__":
    main()
