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

        string += "-------------END-------------\n"
        return string

    def __repr__(self) -> str:
        string = ""
        for product in self.__products:
            string += (str(product)) + "\n"
        return string

    def __iter__(self):
        return iter(self.__products)

    def __len__(self):
        return len(self.__products)

    @property
    def products(self) -> Set[Product]:
        return self.__products

    def is_empty(self) -> bool:
        return len(self) == 0

    def get_product_by_id(self, id: int) -> Product:
        for product in self.__products:
            if id == product.id:
                return product
        raise ValueError(f"Error: Product with id {id} not found.")

    def register_product(self, product: Product) -> None:
        self.__products.add(product)

    def unregister_product(self, product: Product) -> bool:
        try:
            self.__products.remove(product)
            return True
        except KeyError:
            return False

    def unregister_product_by_id(self, id: int) -> bool:
        try:
            product: Product = self.get_product_by_id(id)
            return self.unregister_product(product)
        except ValueError:
            return False
