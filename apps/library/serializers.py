from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'user', 'url', 'created_at', 'updated_at', 'is_public']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate_url(self, value):
        """Ensure each user has unique URLs saved."""
        user = self.context['request'].user
        if Item.objects.filter(user=user, url=value).exists():
            raise serializers.ValidationError("You have already saved this URL.")
        return value
