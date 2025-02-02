from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename="item")

urlpatterns = [
    path('', include(router.urls)),
    path('community/', ItemViewSet.as_view({'get': 'community'}), name='community-feed'),
]