from accounts.models import Transaction, Account, Journal, Ledger, Entry
from rest_framework import serializers

from common.utils import str_is_int

def valid_account(account_identifier):
    if not account_identifier:
        serializers.ValidationError('This field is required.')
        
        
    if str_is_int(account_identifier):
        account = Account.objects.filter(id=account_identifier).first()
    elif type(account_identifier) is str:
        account = Account.objects.filter(slug=account_identifier).first()
    else:
        account = None
        
    if not account or type(account) != Account:
        raise serializers.ValidationError('{} is not a valid account.'.format(account_identifier))
    else:
        return account
        
class TransactionListSerializer(serializers.HyperlinkedModelSerializer):
    account = serializers.CharField(max_length=200, write_only=True, validators=[valid_account])
    timestamp = serializers.DateTimeField(read_only=True, source="created") 
    #  Note: using a reserved keyword here to meet the specified API requirements, but this may be worth reconsidering
    type = serializers.CharField(read_only=True, source="transaction_type")   
    
    class Meta:
        model = Transaction
        fields = ('id','amount','account','timestamp','type')

    def create(self, validated_data):
        account_identifierd = validated_data.pop('account',None)
        account = valid_account(account_identifierd)

        if account:
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
