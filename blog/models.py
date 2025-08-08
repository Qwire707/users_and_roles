from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    text = models.TextField(max_length=1024, verbose_name="Зміст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")

class Comment(models.Model):
    text = models.TextField(max_length=1024, verbose_name="Текст")
    author = models.CharField(max_length=30, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата зміни")

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")

