from rest_framework import serializers

from ExcelToDb.models import Transaction


class TransactionModelMapper(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = '__all__'