from django.db import models
from django.urls import reverse


class Post(models.Model):
    class Meta:
        ordering = ['-created_at']

    POST_TYPE = [
        (0, "해킹"),
        (1, "개발"),
        (2, "보안"),
        (3, "책")
    ]

    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    image = models.ImageField(upload_to='img', blank=True, verbose_name="대표이미지", default="img/bg3.jpg")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="업데이트시간")
    _type = models.PositiveSmallIntegerField(choices=POST_TYPE, verbose_name="게시글타입")

    def value(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.pk])
