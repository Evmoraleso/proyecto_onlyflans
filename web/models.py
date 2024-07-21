from django.db import models
from django.utils.text import slugify
import uuid

class Flan(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    category = models.CharField(
        max_length=50,
        choices=[
            ('tradicional', 'Tradicional'),
            ('innovador', 'Innovador'),
            ('sin_azucar', 'Sin Azúcar'),
        ],
        default='tradicional')
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
            
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.TextField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name