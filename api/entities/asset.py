class Asset():
    def __init__(self, name, modality, price):
        self.__name = name
        self.__modality = modality
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def modality(self):
        return self.__modality

    @modality.setter
    def modality(self, modality):
        self.__modality = modality

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
