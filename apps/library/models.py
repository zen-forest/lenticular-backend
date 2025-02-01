from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import validators  # Extra validation for robust URL checking
from django.conf import settings  # Import settings
# Create your models here.

def validate_strong_url(value):
    """Ensure the URL is valid and has a proper scheme (http/https)."""
    validator = URLValidator(schemes=['http', 'https'])
    try:
        validator(value)
    except ValidationError:
        raise ValidationError("Enter a valid URL starting with http:// or https://")

    # Extra check using the validators package
    if not validators.url(value):
        raise ValidationError("Invalid URL format.")
    

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    url = models.URLField(
        unique=True, 
        validators=[validate_strong_url], 
        help_text="A valid URL starting with http:// or https://",
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the item is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the item is updated

    def __str__(self):
        return self.url

    def get_user(self):
        """Return the user associated with this item."""
        return self.user