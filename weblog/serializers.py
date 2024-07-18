# serializers.py

from rest_framework import serializers
from .models import Post, Comment, Category, Author

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'avatar']

    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}".strip() or obj.user.username

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'content', 'created_at']

class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'categories', 'image', 'created_at', 'updated_at', 'published_at']

class PostDetailSerializer(PostListSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta(PostListSerializer.Meta):
        fields = PostListSerializer.Meta.fields + ['content', 'comments']


class AdjacentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']