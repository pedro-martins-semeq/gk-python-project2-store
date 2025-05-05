from typing import Set
from models.product import Product


class Catalog:
    def __init__(self):
        self.__products: Set[Product] = set()

    def __str__(self) -> str:
        string = "-----------CATALOG-----------\n"
        for product in self.__products:
            string += (
                f"Id: {product.id} - {product.name}\n"
                + f"Price: R$ {product.price:.2f}\n"
                + "=============================\n"
            )

        string += "--------------END--------------\n"
        return string

    def __repr__(self) -> str:
        string = ""
        for product in self.__products:
            string += (str(product)) + "\n"
        return string

    @property
    def products(self) -> Set[Product]:
        return self.__products

    def register_product(self, product: Product) -> None:
        self.__products.add(product)

    def unregister_product(self, product: Product) -> None:
        if product in self.__products:
            self.__products.remove(product)
