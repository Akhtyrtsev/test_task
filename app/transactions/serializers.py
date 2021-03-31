from transactions.models import User, Operation
from transactions.services import get_total_balance
from rest_framework import serializers


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('user', 'amount')

    def create(self, validated_data):
        amount = validated_data['amount']
        operation_type = 'Purchase'
        if amount < 0:
            operation_type = 'Refund'
        validated_data['operation_type'] = operation_type

        return super(TransactionSerializer, self).create(validated_data)


class WithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('user', 'amount')

    def create(self, validated_data):
        validated_data['operation_type'] = 'Withdrawal'
        amount = validated_data['amount']
        amount = abs(amount)  # make amount always positive in order to compare with current balance
        user = validated_data['user']
        total_balance = get_total_balance(user)
        if total_balance < amount:
            raise serializers.ValidationError('Amount should be less or equal to total balance')
        amount = -1 * amount  # save amount as negative value
        validated_data['amount'] = amount
        return super(WithdrawalSerializer, self).create(validated_data)