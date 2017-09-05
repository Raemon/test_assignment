from rest_framework import routers
from .viewsets import AccountViewSet, TransactionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)