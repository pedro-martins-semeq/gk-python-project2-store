class Product:
    __counter: int = 1

    def __init__(self, name: str, price: float) -> None:
        self.__id: int = Product.__counter
        Product.__counter += 1

        self.__name: str = name
        self.__price: float = price

    def __str__(self):
        return f"Id: {self.id} | Name: {self.name} | Price: R${self.price}"

    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id

    def __hash__(self):
        return hash(self.id)

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price
