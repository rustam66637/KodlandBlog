from django.db import models

"""
Post
------------
title, slug, content, image, publish_date
"""

class Post(models.Model):
    '''Статьи'''
    title = models.CharField('Заголовок', max_length=150)
    slug = models.SlugField('URL', max_length=150, unique=True)
    content = models.TextField('Содержание', max_length=5000, blank=True)
    image = models.ImageField('Изображение', upload_to='media/images/%Y/%m/%d/', blank=True)
    publish_date = models.DateTimeField('Публикация', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-publish_date',)

