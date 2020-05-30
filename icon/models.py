from django.db import models
from gallery import settings
from django.contrib.auth.models import User


class Picture(models.Model):

    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    image = models.ImageField(verbose_name='Изображение', null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')

    def __str__(self):
        return self.name


class Comment(models.Model):

    text = models.CharField(max_length=256, verbose_name='комментарий')
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='комментарий', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')

    def __str__(self):
        return self.text


class Like(models.Model):

    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, verbose_name='лайк', related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')

