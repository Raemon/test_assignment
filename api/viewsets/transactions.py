from ..serializers import TransactionDetailSerializer, TransactionListSerializer
from rest_framework.viewsets import ModelViewSet
from accounts.models import Transaction
from .utils import MultiSerializerViewSet

class TransactionViewSet(MultiSerializerViewSet):
    model = Transaction
    queryset = Transaction.objects.filter(is_enabled=True)
    
    serializers = {
        'default': TransactionListSerializer,
        'retrieve': TransactionDetailSerializer
    }
    
    lookup_field = 'id'

    