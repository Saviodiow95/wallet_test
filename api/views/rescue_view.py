from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from api.entities import rescue
from api.serializers.rescue_serializer import RescueSerializer
from api.services import rescue_service, wallet_service


class RescueList(APIView):
    """
    Todos os métodos so podem ser executados caso o usuário esteja autenticado.
    O método get é usado para listar os resgates
    o método post é usado para criar/realizar as resgates
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
       Retorna uma lista de resgates com base no usuário que as realizou
       :param request:
       :param format:
       :return:
       """
        user = request.user
        rescues = rescue_service.list_rescue(user)
        serializer = RescueSerializer(rescues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
       Cria um novo resgate
       :param request:
       :param format:
       :return:
       """
        serializer = RescueSerializer(data=request.data)
        if serializer.is_valid():
            wallet = wallet_service.wallet_list(request.user)
            asset = serializer.validated_data['asset']
            amount = serializer.validated_data['amount']
            price_unit = serializer.validated_data['price_unit']
            ip_access = request.META['REMOTE_ADDR']
            rescue_new = rescue.Rescue(wallet, asset, amount, price_unit, ip_access)
            rescue_db = rescue_service.create_rescue(rescue_new)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
