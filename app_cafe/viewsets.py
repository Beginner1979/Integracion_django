from rest_framework.viewsets import ModelViewSet
from .models import Cafe
from .serializers import CafeSerializer

class CafeViewSet(ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer