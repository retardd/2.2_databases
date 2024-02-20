from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название тэга')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tags, related_name='article', through='CollectTags')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class CollectTags(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='collecttags')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='collecttags')
    maintag = models.BooleanField(default=False, verbose_name='основной')