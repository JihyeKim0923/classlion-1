from .models import Post,Product
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('title', 'body')
        #read_only_fields=('title',)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('title', 'body','price')
        #read_only_fields=('title',)
        