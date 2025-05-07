from utils.catalog import Catalog
from utils.cart import Cart
from models.product import Product
from typing import Dict
from os import name as _os_name, system as _os_system


def clear():
    _os_system("cls" if _os_name == "nt" else "clear")


def input_uint(prompt: str) -> int:
    while True:
        buff: str = input(prompt + "\n> ")

        try:
            value: int = int(buff)

            if value < 0:
                print("Invalid number. Enter a positive integer number.")
                continue
            break
        except (TypeError, ValueError):
            print(
                (
                    "Invalid number ("
                    + f'"{(buff[:12] + "[...]") if len(buff) > 12 else buff}"'
                    + " was given)."
                    + " Please enter a valid integer number..."
                )
            )
    return value


def input_ufloat(prompt: str) -> float:
    while True:
        buff: str = input(prompt + "\n> ")

        try:
            value: float = float(buff.strip().replace(",", "."))

            if value < 0:
                print("Invalid number. Enter a positive decimal number.")
                continue
            break
        except (TypeError, ValueError):
            print(
                (
                    "Invalid number ("
                    + f'"{(buff[:12] + "[...]") if len(buff) > 12 else buff}"'
                    + " was given)."
                    + "Please enter a valid decimal number "
                    + '(use a single "." or "," as separator).'
                )
            )
    return value


def continue_lock() -> None:
    _: str = input("Press <enter> to continue...")
    return None


def print_store_header():
    string: str = "========PRODUCT_STORE========"
    clear()
    print(string)


def option_select_form(options: Dict[int, str]) -> int:
    print_store_header()

    for key, value in options.items():
        print(f"[{key}] - {value}")

    while True:
        option: int = input_uint("Choose an option: ")

        if option in options:
            return option
        else:
            print("Invalid option...")


def register_catalog_product_form(catalog: Catalog) -> None:
    print_store_header()

    p_name: str = input("Product name: \n> ")
    p_price: float = input_ufloat("Product Price (in R$):")

    product = Product(p_name, p_price)
    catalog.register_product(product)

    print(f"{str(product)}\n" + "was successfully added to catalog.\n")


def unregister_catalog_product_form(catalog: Catalog) -> None:
    print_store_header()
    print(repr(catalog))

    print("Select the product you want to remove by providing its ID.")

    while True:
        p_id = input_uint("Product ID:")

        try:
            _: bool = catalog.unregister_product_by_id(p_id)
            break
        except ValueError:
            print(f"Product with id {p_id} not found.")

    print(
        f"Product with Id: {str(p_id)} " +
        " was successfully removed from catalog.\n"
    )


def show_product_catalog(catalog: Catalog) -> None:
    print(str(catalog))


def add_product_to_cart_form(catalog: Catalog, cart: Cart) -> None:
    print_store_header()
    show_product_catalog(catalog)

    show_cart_items(cart)
    print()

    print("Select a product to add to your cart by providing it's ID.")

    while True:
        p_id = input_uint("Product ID:")

        try:
            product = catalog.get_product_by_id(p_id)
            cart.add_product(product)
            break
        except ValueError:
            print(f"Product with id {p_id} not found.")

    print(f"Product with Id: {str(p_id)} " +
          " was successfully added to cart.\n")


def remove_product_from_cart_form(catalog: Catalog, cart: Cart) -> None:
    print_store_header()

    show_cart_items(cart)

    print("Select a product to remove from your cart by providing it's ID.")

    while True:
        p_id = input_uint("Product ID:")
        try:
            product = catalog.get_product_by_id(p_id)
            if cart.remove_product(product):
                print(
                    f"Product with Id: {str(p_id)} "
                    + " was successfully added to cart.\n"
                )
                break
            else:
                print(f"Product with id {p_id} not found in your cart.")
        except ValueError:
            print(f"Product with id {p_id} not found in catalog.")


def show_cart_items(cart: Cart) -> None:
    for key, qty in cart.products.items():
        print(
            f"{key.id} - {key.name} |- R$ {key.price:.2f} {qty}x "
            + f"= {(key.price * qty):.2f}"
        )

    print("\n")
    print(f"TOTAL: R${cart.total:.2f}\n")


def main():
    options: Dict[int, str] = {
        1: "Register Product",
        2: "Unregister Product",
        3: "Show Product Catalog",
        4: "Add Product to Cart",
        5: "Remove Product from Cart",
        6: "Show Cart Items",
        0: "Exit",
    }

    catalog: Catalog = Catalog()
    cart: Cart = Cart()

    while True:
        option = option_select_form(options)

        if option == 1:
            register_catalog_product_form(catalog)
            continue_lock()
        elif option == 2:
            if catalog.is_empty():
                print("No Product registered on Catalog.")
                continue_lock()
            else:
                unregister_catalog_product_form(catalog)
                continue_lock()
        elif option == 3:
            print_store_header()
            show_product_catalog(catalog)
            continue_lock()
        elif option == 4:
            add_product_to_cart_form(catalog, cart)
            continue_lock()
        elif option == 5:
            if cart.is_empty():
                print("Empty Cart.")
                continue_lock()
            else:
                remove_product_from_cart_form(catalog, cart)
                continue_lock()
        elif option == 6:
            print_store_header()
            show_cart_items(cart)
            continue_lock()
        elif option == 0:
            input("Exiting program...")
            break


if __name__ == "__main__":
    main()
