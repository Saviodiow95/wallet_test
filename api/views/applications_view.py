from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from api.entities import application
from api.serializers.application_serializer import ApplicationSerializer
from api.services import application_service, wallet_service


class ApplicationList(APIView):
    """
    Todos os métodos so podem ser executados caso o usuário esteja autenticado.
    O método get é usado para listar as aplicações
    o método post é usado para criar/realizar as aplicações
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Retorna uma lista de aplicações com base no usuário que as realizou
        :param request:
        :param format:
        :return:
        """
        user = request.user
        applications = application_service.list_application(user)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Cria uma nova aplicação
        :param request:
        :param format:
        :return:
        """
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            wallet = wallet_service.wallet_list(request.user)
            asset = serializer.validated_data['asset']
            amount = serializer.validated_data['amount']
            price_unit = serializer.validated_data['price_unit']
            ip_access = request.META['REMOTE_ADDR']
            application_new = application.Application(wallet, asset, amount, price_unit, ip_access)
            application_db = application_service.create_application(application_new)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
