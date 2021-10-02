from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("post.urls", namespace="post")),
    path("", RedirectView.as_view(url="/posts")),
]
