from django.db import models


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория"
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"
