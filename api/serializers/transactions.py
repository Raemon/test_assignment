from accounts.models import Transaction, Account, Journal, Ledger, Entry
from rest_framework import serializers

class TransactionListSerializer(serializers.HyperlinkedModelSerializer):
    account = serializers.CharField(max_length=200, write_only=True)
    timestamp = serializers.DateTimeField(read_only=True, source="created")  
    type = serializers.CharField(label="type", read_only=True, source="transaction_type")   
    
    class Meta:
        model = Transaction
        fields = ('id','amount','account','timestamp','type')

    def create(self, validated_data):
        account_slug = validated_data.pop('account')
        account = Account.objects.filter(slug=account_slug).first()
        validated_data['account_id'] = account.id
        validated_data['journal_id'] = account.journal.id
        
        obj = Transaction.objects.create(**validated_data)
        obj.save()
        return obj

class TransactionDetailSerializer(TransactionListSerializer):
    timestamp = serializers.DateTimeField(read_only=True, source="created")
    type = serializers.CharField(label="type", read_only=True, source="transaction_type")   
    
    class Meta(TransactionListSerializer.Meta):
        fields = ('id','amount','timestamp','type')

