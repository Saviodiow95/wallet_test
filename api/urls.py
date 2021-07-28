from django.urls import path

from api.views.applications_view import ApplicationList
from api.views.asset_view import AssetList, AssetDetail, AssetListModality
from api.views.rescue_view import RescueList
from api.views.wallet_view import WalletList

urlpatterns = [
    path('asset/', AssetList.as_view(), name='asset_list'),
    path('asset/<int:pk>', AssetDetail.as_view(), name='asset_detail'),
    path('asset/<str:modality>', AssetListModality.as_view(), name='asset_list_modality'),

    path('wallet/', WalletList.as_view(), name='wallet_list'),

    path('application/', ApplicationList.as_view(), name='application_list'),

    path('rescue/', RescueList.as_view(), name='rescue_list'),

]
