from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from blog.models import Post

from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
)
from .permissions import OwnerOrReadOnly

class PostCreateApiView(CreateAPIView): 
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class PostListApiView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer   

class PostDetailApiVIew(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer 
    lookup_field = 'slug'
    lookup_url_kwarg = 'post_slug'  

class PostDeleteApiVIew(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer 
    lookup_field = 'slug'
    lookup_url_kwarg = 'post_slug' 

class PostUpdateApiVIew(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer   
    lookup_field = 'slug'
    lookup_url_kwarg = 'post_slug' 
    permission_classes = [OwnerOrReadOnly]
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)  

