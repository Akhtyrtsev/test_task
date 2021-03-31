from django.shortcuts import render

from rest_framework import views, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from transactions.models import Operation
from transactions.serializers import OperationSerializer, WithdrawalSerializer, TransactionSerializer
from transactions.paginators import OperationPagination, GeneralPagination


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all().order_by('-date_created')
    serializer_class = OperationSerializer
    pagination_class = OperationPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-date_created')


class WithdrawalViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.filter(operation_type='Withdrawal')
    serializer_class = WithdrawalSerializer
    pagination_class = GeneralPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-date_created')


# Webhook
@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
def transactions(request):
    serializer = TransactionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)