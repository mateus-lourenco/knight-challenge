from django.urls import path, include
from rest_framework import routers

from .viewsets import PieceViewSet

router = routers.DefaultRouter()
router.register(r'pieces', PieceViewSet, basename='piece')

urlpatterns = [
    path('api/', include(router.urls)),
]