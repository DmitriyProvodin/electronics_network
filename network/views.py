from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import NetworkNode
from .serializers import NetworkNodeSerializer
from .permissions import IsActiveEmployee
from .filters import NetworkNodeFilter


class NetworkNodeViewSet(ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NetworkNodeFilter
