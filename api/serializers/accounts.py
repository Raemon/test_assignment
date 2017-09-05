from accounts.models import Account
from rest_framework import serializers

class AccountListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'name', 'slug')

class AccountDetailSerializer(AccountListSerializer):
    
    class Meta(AccountListSerializer.Meta):
        fields = ('id', 'name', 'slug',)
