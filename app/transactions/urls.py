from django.urls import include, path
from rest_framework import routers

from transactions.views import OperationViewSet, WithdrawalViewSet, transactions
router = routers.DefaultRouter()

router.register('operations', OperationViewSet, basename='operations')
router.register('withdrawals', WithdrawalViewSet, basename='withdrawals')

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('rest_registration.api.urls')),
    path('accounts/', include('rest_registration.api.urls')),
    path('transactions/', transactions, name='transactions')
    ]