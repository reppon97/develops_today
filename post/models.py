from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    link = models.URLField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    class Meta:
        ordering = ("-pk",)

    def count_likes(self):
        return Like.objects.filter(post=self).count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ("-pk",)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("author", "post")
        ordering = ("-pk",)

    def __str__(self):
        return self.post.title
