from django.db import models
from users.models import User

# Create your models here.

def contact_default():
    return ("to1@example.com")

class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # email = models.TextField(default = contact_default(), auto_created=True)
    
    def __str__(self) -> str:
        return f"{self.id} {self.title}"

    class Meta:
        db_table = 'categories'

class Task(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
         User, on_delete=models.CASCADE, null=True, blank=True
     )
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        null=True,
        blank=True,
        choices=[
            ('created', 'Creado'),
            ('in_progress', 'En Progreso'),
            ('finished', 'Terminado')
        ]
    )
    color = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} {self.title}"

    class Meta:
        db_table = 'tasks'