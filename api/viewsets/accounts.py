from ..serializers import AccountDetailSerializer, AccountListSerializer
from rest_framework.viewsets import ModelViewSet
from accounts.models import Account
from .utils import MultiSerializerViewSet

class AccountViewSet(MultiSerializerViewSet):
    model = Account
    queryset = Account.objects.filter(is_enabled=True)

    serializers = {
        'default': AccountListSerializer,
        'retrieve': AccountDetailSerializer
    }

    lookup_field = 'id'

    