from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from api.serializers.wallet_serializer import WalletSerializer
from api.services import wallet_service


class WalletList(APIView):
    """
    Todos o métodos serão executados apenas se o usuário estiver autenticado
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Busca uma carteira de acordo com o usuário autenticado
        :param request:
        :param format:
        :return:
        """
        user = request.user
        wallet = wallet_service.wallet_list(user)
        serializer = WalletSerializer(wallet, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
