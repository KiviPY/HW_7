from datetime import datetime

from django.db import models

# Create your models here.

class Articles(models.Model):
    __tablename__ = 'articles'

    title: str = models.CharField('Название', max_length=50, null=False, blank=False)
    anons: str = models.CharField('Анонс', max_length=250,  blank=True)
    full_text: str = models.TextField('Статья', null=False, blank=False)
    date: datetime = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

