from rest_framework.exceptions import APIException


class InsufficientFundsException(APIException):
    """
    Exceção criada para retornar uma mensagem quando não houver saldo de um ativo para realizar o resgate
    """
    status_code = 304
    default_detail = 'Não é possível realizar o Resgate, Saldo Insuficiente'
