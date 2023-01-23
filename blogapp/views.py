from rest_framework.viewsets import ModelViewSet
from .models import CategoryModel, BlogModel
from .serializers import CategorySerializers, BlogSerializers


class CategoryView(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers


class BlogView(ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
