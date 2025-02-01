from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to CRUD their saved creative items.
    """
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Ensure users can only access their own saved items."""
        return Item.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically associate the logged-in user with the new item."""
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        """Ensure users can only update their own items."""
        instance = get_object_or_404(Item, id=kwargs["pk"], user=request.user)
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """Ensure users can only partially update their own items."""
        instance = get_object_or_404(Item, id=kwargs["pk"], user=request.user)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Ensure users can only delete their own items."""
        instance = get_object_or_404(Item, id=kwargs["pk"], user=request.user)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
