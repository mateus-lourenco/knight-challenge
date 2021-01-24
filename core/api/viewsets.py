
from rest_framework.viewsets import ModelViewSet

from .serializers import PieceSerializer
from core.models import Piece


class PieceViewSet(ModelViewSet):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer