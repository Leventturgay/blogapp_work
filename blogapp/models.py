from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
