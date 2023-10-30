from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    # created_at = models.CharField(max_length=100, **NULLABLE)

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(auto_now=False, auto_now_add=True, max_length=100, verbose_name='Дата создания')
    last_modified_date = models.DateField(auto_now=True, auto_now_add=False, max_length=100, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
