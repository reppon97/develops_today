from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

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


class LikeAPIView(APIView):
    def get_object(self, like_id):
        try:
            return Like.objects.get(id=like_id)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def get(request):
        votes = Like.objects.all()
        serializer = LikeSerializer(votes, many=True)

        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        like = self.get_object(pk)
        like.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
