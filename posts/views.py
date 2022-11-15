from django.contrib.auth import get_user_model
from django.views.generic import ListView
from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostList(generics.ListCreateAPIView):
    """
    Display a list of :model:`posts.Post`.

    **Context**

    ``Post``
        An instance of :model:`posts.Post`

    **Template**

    :template:`posts/post_list.html`
    """

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"

    paginate_by = 5
