from rest_framework import generics

from post.models import Post, Comment, Like
from post.serializer import PostSerializer, CommentSerializer, LikeSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new post.
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post instance.
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentList(generics.ListCreateAPIView):
    """
    List all posts or create a new comment.
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a comment
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class LikeList(generics.ListCreateAPIView):
    """
    List all posts or create a new like.
    """

    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a like
    """

    serializer_class = LikeSerializer
    queryset = Like.objects.all()
