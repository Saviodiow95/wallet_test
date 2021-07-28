from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from api.entities import asset as asset_entitie
from api.serializers.asset_serializer import AssetSerializer
from api.services import asset_service



class AssetList(APIView):
    """
    Todos os métodos so podem ser executados caso o usuário esteja autenticado.
    O método get é usado para listar os ativos cadastrados
    O método post é usado para criar novos ativos
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Lista todos os ativos cadastrados
        :param request:
        :param format:
        :return:
        """
        assets = asset_service.list_assets()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """
        Cadastra um novo ativo
        :param request:
        :param format:
        :return:
        """
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            modality = serializer.validated_data['modality']
            price = serializer.validated_data['price']
            asset_new = asset_entitie.Asset(name, modality, price)
            asset_db = asset_service.create_asset(asset_new)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetDetail(APIView):
    """
    Todos os métodos so podem ser executados caso o usuário esteja autenticado.
    O metodo get retorna um ativo pelo id
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        """
        Busca e retorna um ativo pelo id passado
        :param request:
        :param pk: id do ativo desejado
        :type pk: int
        :param format:
        :return:
        """
        asset = asset_service.list_asset_id(pk)
        serializer = AssetSerializer(asset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        Edita o ativo de acordo passando o id pela url
        :param request:
        :param pk:
        :param format:
        :return:
        """
        asset_old = asset_service.list_asset_id(pk)
        serializer = AssetSerializer(asset_old, data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            modality = serializer.validated_data['modality']
            price = serializer.validated_data['price']
            asset_new = asset_entitie.Asset(name=name, modality=modality, price=price)
            asset_service.edit_asset(asset_old=asset_old, asset_new=asset_new)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetListModality(generics.ListAPIView):
    """
     Todos os métodos so podem ser executados caso o usuário esteja autenticado.
     Esta classe retorna uma lista com todos os ativos de acordo com a modalidade informada.
     """
    permission_classes = [IsAuthenticated]
    serializer_class = AssetSerializer

    def get_queryset(self):
        """
        Retorna uma lista de ativos de acordo com a modalidade passada na URL
        """
        modality = self.kwargs.get('modality')
        return asset_service.list_asset_modality(modality)
