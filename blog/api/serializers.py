from rest_framework import serializers 
from blog.models import Post

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            # 'published',
        ]

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = [
            'id',
            'author',
            'title',
            'slug',
            'content',
            'published',
        ]
        
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = [
            'id',
            'author', 
            'title',
            'slug',
            'content',
            'published',
        ]


