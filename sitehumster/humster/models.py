from django.db import models


class humster(models.Model):
    title = models.CharField(max_length=255, verbose_name='ФИО')
    content = models.TextField(blank=True, verbose_name='О человеке')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='время обновления')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')


    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

class Kvantorium(models.Model):
    surname = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    patronymic = models.CharField(max_length=10, blank=True)
    Birthday = models.DateTimeField(max_length=15)
    is_excellent = models.BooleanField(max_length=15)
    is_not_excellent = models.BooleanField(max_length=15)

class Favourite_book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    summary = models.TextField(default=True, verbose_name='Что происходит в книге')
    author = models.CharField(max_length=30, verbose_name='Автор')
    price = models.IntegerField(verbose_name='Цена')
    interesting = models.BooleanField(default=True, verbose_name='✅ или ❌')

    class Meta:
        verbose_name = 'любимые книги'
        verbose_name_plural = 'любимые книги'

