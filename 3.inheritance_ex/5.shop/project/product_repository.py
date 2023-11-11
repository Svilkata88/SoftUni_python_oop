from typing import List

from project.product import Product


class ProductRepository:
    products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name) -> Product:
        product = [p for p in self.products if p.name == product_name]
        return product[0]

    def remove(self, product_name):
        for obj in self.products:
            if obj.name == product_name:
                self.products.remove(obj)

    def __repr__(self):
        return '\n'.join([f'{p.name}: {p.quantity}' for p in self.products])


