from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import Prefetch
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostListSerializer, PostDetailSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['categories']
    ordering_fields = ['published_at', 'created_at']
    search_fields = ['title', 'description']

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True) \
            .select_related('author__user') \
            .prefetch_related('categories') \
            .prefetch_related(
                Prefetch('comments', queryset=Comment.objects.filter(approved=True))
            )
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer


    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'], approved=True)

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['post_pk'])

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]