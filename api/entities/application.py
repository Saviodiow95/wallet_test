class Application():
    def __init__(self, wallet, asset, amount, price_unit, ip_access):
        self.__wallet = wallet
        self.__asset = asset
        self.__amount = amount
        self.__price_unit = price_unit
        self.__ip_access = ip_access

    @property
    def wallet(self):
        return self.__wallet

    @wallet.setter
    def wallet(self, wallet):
        self.__wallet = wallet

    @property
    def asset(self):
        return self.__asset

    @asset.setter
    def asset(self, asset):
        self.__asset = asset

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def price_unit(self):
        return self.__price_unit

    @price_unit.setter
    def price_unit(self, price_unit):
        self.__price_unit = price_unit

    @property
    def ip_access(self):
        return self.__ip_access

    @ip_access.setter
    def ip_access(self, ip_access):
        self.__ip_access = ip_access

