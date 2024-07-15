# urls.py

from django.urls import path, include
from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')  # Add basename here
router.register(r'categories', CategoryViewSet)

posts_router = routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]