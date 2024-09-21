from django.db import models
from django.urls import reverse_lazy


class Tasks(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Контент')
    tip = models.TextField(blank=True, verbose_name='Подсказка')
    solve = models.TextField(blank=True, verbose_name='Решение')
    reply = models.TextField(blank=True, verbose_name='Ответ')
    themes = models.TextField(blank=False, verbose_name='Категории')
    difficulty = models.CharField(max_length=10, verbose_name='Сложность')
    classes = models.CharField(max_length=20, verbose_name='Сложность')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('view_tasks', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        # ordering = ["-created_at"]


# class Category(models.Model):
#    title = models.CharField(max_length=150, db_index=True, verbose_name='Название категорий')
#
#    def __str__(self):
#        return self.title
#
#    def get_absolute_url(self):
#        return reverse_lazy('category', kwargs={'category_id': self.pk})
#
#    class Meta:
#        verbose_name = 'Категория'
#        verbose_name_plural = 'Категории'
#        ordering = ["title"]
