class Store:
    def __init__(self):
        self.products = []
        self.users = {}

    def authorise(self, login, password):
        return login in self.users.keys() and self.users[login].password == password

    def add_product(self, product: str):
        self.products.append(product)

    def buy_product(self, product: str):
        try:
            index = self.products.index(product)
        except ValueError:
            return None

        return self.products.pop(index)
    
    def get_products(self):
        return self.products


class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


class Client:
    def __init__(self, name: str):
        self.name = name
        self.bought = []
        self.password = {}

    def buy_product(self, store: Store, product: str):
        bought = store.buy_product(product)
        if bought is not None:
            self.bought.append(bought)
        else:
            print("Warning, there is no such product available!")

    def view_products(self):
        return self.bought



class Admin:
    def __init__(self, name: str):
        self.name = name
    
    def add_product(self, store: Store, product: str):
        store.products.append(product)
