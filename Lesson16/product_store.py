from enum import StrEnum
from typing import List
from collections import defaultdict


class ProductType(StrEnum):
    SPORT = "Sport"
    FOOD = "Food"
    ELECTRONICS = "Electronics"
    COMPUTERS = "Computers"
    FASHION = "Fashion"
    PETS = "Pets"
    TOYS = "Toys"
    GAMES = "Games"
    BEAUTY = "Beauty"


class Product:
    def __init__(self, product_type: ProductType, name: str, price: float):
        self.product_type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.__income = 0
        self.__product_to_amount = defaultdict(int)
        self.__product_types = [product_type.title() for product_type in ProductType]

    def add(self, product: Product, amount: int):
        if product.name in self.__product_to_amount:
            self.__product_to_amount[product] += amount
        else:
            self.__product_to_amount[product] = amount

    def get_product_info(self, product_name: str):
        for product in self.__product_to_amount.keys():
            if product.name == product_name:
                return product.name, self.__product_to_amount[product]
        raise ValueError(f"Product {product_name} was sold out")

    def set_discount(self, identifier: str | ProductType, percent: int, identifier_type="name"):

        if identifier_type not in ["name", "type"]:
            raise ValueError("Wrong identifier type")

        if identifier_type == "type" and identifier not in self.__product_types:
            raise ValueError("Wrong filter type")

        filtered_products_by_identifier = list(filter(lambda p: p.name == identifier if identifier_type == "name" else
        p.product_type == identifier, self.__product_to_amount.keys()))
        if len(filtered_products_by_identifier) == 0:
            raise ValueError(f"Sorry, all {identifier} products were sold out! Impossible to set a discount.")

        for product in filtered_products_by_identifier:
            product.price -= product.price * (percent / 100)

    def sell_product(self, product_name: str, amount: int):
        found_products_by_name = list(filter(lambda p: p.name == product_name, self.__product_to_amount.keys()))

        if len(found_products_by_name) == 0:
            raise ValueError(f"Sorry, the product was not found! Impossible to sell")

        for found_product in found_products_by_name:
            if amount > self.__product_to_amount[found_product]:
                raise ValueError(f"Impossible to sell {product_name}. Provided amount {amount}, "
                                 f"{self.__product_to_amount[found_product]} available")

            self.__product_to_amount[found_product] -= amount
            self.__income += amount * found_product.price

    def get_income(self):
        return self.__income

    def get_all_products(self):
        return [(product.product_type, product.name, product.price, amount) for product, amount in
                self.__product_to_amount.items()]


if __name__ == "__main__":
    p = Product(ProductType.SPORT, "Football T-Shirt", 100)

    p2 = Product(ProductType.FOOD, "Ramen", 1.5)

    s = ProductStore()
    s.add(p, 10)
    s.add(p2, 300)

    print(s.get_product_info("Football T-Shirt"))
    print(s.get_all_products())
    s.set_discount(ProductType.SPORT, 10, "type")
    s.set_discount("Football T-Shirt", 15, "name")
    print(s.get_all_products())
    s.sell_product("Ramen", 3)
    s.sell_product("Football T-Shirt", 9)
    print(s.get_all_products())
    print(s.get_income())
