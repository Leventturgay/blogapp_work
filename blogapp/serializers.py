from rest_framework import serializers
from .models import CategoryModel, BlogModel


class CategorySerializers(serializers.ModelSerializer):
    class Meta:

        model = CategoryModel
        fields = ('id', 'name')


class BlogSerializers(serializers.ModelSerializer):
    class Meta:

        model = BlogModel
        fields = ('id', 'title', 'description', 'created_date', 'updated_date')
