from typing import Dict
from models.product import Product


class Cart:
    def __init__(self) -> None:
        self.__products: Dict[Product, int] = dict()
        self.__total: float = 0

    @property
    def products(self) -> Dict[Product, int]:
        return self.__products

    @property
    def total(self) -> float:
        return self.__total

    def __len__(self):
        return len(self.__products)

    def is_empty(self) -> bool:
        return len(self) == 0

    def add_product(self, product: Product) -> None:
        if product in self.products.keys():
            self.products[product] += 1
        else:
            self.products[product] = 1
        self.__total += product.price

    def remove_product(self, product: Product) -> bool:
        if product in self.products:
            self.products[product] -= 1
            if self.products[product] <= 0:
                del self.products[product]
            self.__total -= product.price
            return True
        else:
            return False
