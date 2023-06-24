class Product():

    def __init__(self, id, name, description, quantity, price, category):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__quantity = quantity

    def __int__(self):
        pass

    def view(self):
        return f"{self.__id} {self.__name} {self.__description} {self.__price} {self.__category} {self.__quantity}"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        self.__category = category

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description