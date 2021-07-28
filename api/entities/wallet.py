class Wallet():
    def __init__(self, user):
        self.__user = user

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

