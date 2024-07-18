from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import Prefetch
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostListSerializer, PostDetailSerializer, CommentSerializer, AdjacentPostSerializer
from .pagination import StandardResultsSetPagination

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['categories']
    ordering_fields = ['published_at', 'created_at']
    search_fields = ['title', 'description']
    pagination_class = StandardResultsSetPagination

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
        elif self.action == 'adjacent_posts':
            return AdjacentPostSerializer
        return PostDetailSerializer

    @action(detail=True, methods=['get'])
    def adjacent_posts(self, request, pk=None):
        current_post = self.get_object()
        
        # Get the previous post
        previous_post = Post.objects.filter(
            is_published=True,
            published_at__lt=current_post.published_at
        ).order_by('-published_at').first()

        # Get the next post
        next_post = Post.objects.filter(
            is_published=True,
            published_at__gt=current_post.published_at
        ).order_by('published_at').first()

        # Serialize the posts
        previous_serializer = self.get_serializer(previous_post) if previous_post else None
        next_serializer = self.get_serializer(next_post) if next_post else None

        return Response({
            'previous': previous_serializer.data if previous_serializer else None,
            'next': next_serializer.data if next_serializer else None
        })

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'], approved=True)

    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['post_pk'])

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]