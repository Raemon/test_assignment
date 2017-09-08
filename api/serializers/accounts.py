from accounts.models import Account, Ledger, Journal, Entry
from rest_framework import serializers
from .transactions import TransactionDetailSerializer

class AccountListSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(write_only=True)
    slug = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('id', 'name', 'slug',)
        

class AccountDetailSerializer(AccountListSerializer):
    principal = serializers.SerializerMethodField()
    
    transactions = TransactionDetailSerializer(many=True, read_only=True)
    
    class Meta(AccountListSerializer.Meta):
        fields = ('id', 'name', 'slug', 'principal', 'transactions',)

    def get_principal(self, obj):
        principal = obj.journal.ledgers.filter(name=Ledger.PRINCIPAL).first()
        principal_entries = principal.entries.all()
        return sum([x.amount for x in principal_entries])