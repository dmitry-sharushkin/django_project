from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True, max_length=100, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='публикация')
    views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
