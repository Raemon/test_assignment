from accounts.models import Transaction
from rest_framework import serializers

class TransactionListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ('id',)

class TransactionDetailSerializer(TransactionListSerializer):
    
    class Meta(TransactionListSerializer.Meta):
        fields = ('id',)
