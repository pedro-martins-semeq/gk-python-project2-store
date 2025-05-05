from utils.catalog import Catalog
from utils.cart import Cart
from models.product import Product
from typing import List, Dict
from os import name as _os_name, system as _os_system


def clear():
    _os_system("cls" if _os_name == "nt" else "clear")


def print_store_header():
    string: str = "=======PRODUCT_STORE======="
    print(string)


def option_select_form(options: Dict[int, str]) -> int:
    clear()
    print_store_header()

    for key, value in options.items():
        print(f"[{key}] - {value}")

    while True:
        try:
            buffer: str = input("> ")
            option: int = int(buffer)

            if option in options:
                return option
            else:
                print("Invalid option...")

        except (ValueError, TypeError) as e:
            print(f"Error: {e}")


def register_catalog_product_form(catalog: Catalog) -> None:
    clear()
    print_store_header()

    p_name: str = input("Product name: \n> ")

    buffer: str = ""
    print("Product price: ")

    while True:
        try:
            buffer = input("> R$ ")
            buffer = buffer.replace(",", ".").strip()
            p_price: float = float(buffer)
        except (ValueError, TypeError) as e:
            print(f"[Error: {e}]Please, enter a valid price...")
            continue
        except:
            input("Unknown Error!")
            exit(1)
        break

    product = Product(p_name, p_price)
    catalog.register_product(product)

    input(f"{str(product)} was successfully added to catalog.")


def unregister_catalog_product_form(catalog: Catalog) -> None:
    clear()
    print_store_header()
    print(repr(catalog))

    print("Select the product you want to remove by providing it's ID.")

    buffer: str = ""
    print("Product ID: ")

    while True:
        try:
            buffer = input("> ")
            buffer = buffer.strip()
            p_id: int = int(buffer)
        except (ValueError, TypeError) as e:
            print(f"[Error: {e}]Please, enter a valid id...")
            continue
        except:
            input("Unknown Error!...")
            exit(1)
        break

    for product in catalog.products:
        if p_id == product.id:
            catalog.unregister_product(product)
            input(f"{str(product)} was successfully removed from catalog...")
            break


def show_product_catalog(catalog: Catalog) -> None:
    clear()
    print_store_header()
    input(str(catalog) + "\n press <enter> to continue...")


def add_product_to_cart_form(catalog: Catalog, cart: Cart) -> None:
    pass


def remove_product_from_cart_form(catalog: Catalog, cart: Cart) -> None:
    pass


def show_cart_items(cart: Cart) -> None:
    pass


def get_total_value_report(cart: Cart) -> None:
    pass


def main():
    options: Dict[int, str] = {
        1: "Register Product",
        2: "Unregister Product",
        3: "Show Product Catalog",
        0: "Exit",
    }

    catalog: Catalog = Catalog()
    cart: Cart = Cart()

    while True:
        option = option_select_form(options)

        if option == 1:
            register_catalog_product_form(catalog)
        elif option == 2:
            unregister_catalog_product_form(catalog)
        elif option == 3:
            show_product_catalog(catalog)
        elif option == 0:
            input("Exiting program...")
            break


if __name__ == "__main__":
    main()
