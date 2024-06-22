from .models import Category, Task

from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category    
        fields = (
            'id',
            'title',
            'description'
        )

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        ## fields = '__all__'  -------> Tambien funciona pra todos los campos a visualizar
        fields = (
            'id',
            'title',
            'category',
            'user',            
            'description',
            'status',
        )

