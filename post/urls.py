from django.urls import path

from post import views

app_name = "post"

urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/<int:pk>", views.PostDetail.as_view()),
    path("comments/", views.CommentList.as_view()),
    path("comments/<int:pk>", views.CommentDetail.as_view()),
    path("likes/", views.LikeList.as_view()),
    path("likes/<int:pk>", views.LikeDetail.as_view()),
]
