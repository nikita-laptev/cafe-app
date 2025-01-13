from django.db import models
from django.conf import settings


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_name = models.CharField(max_length=250, verbose_name="Название статуса")

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.status_name


class CookingStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    cooking_status_name = models.CharField(max_length=250, verbose_name="Название статуса")

    class Meta:
        verbose_name = 'Статус приготовления'
        verbose_name_plural = 'Статусы приготовления'

    def __str__(self):
        return self.cooking_status_name


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Дата и время заказа")
    waiter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Официант"
    )
    status = models.ForeignKey(
        'Status', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Статус"
    )
    cooking_status = models.ForeignKey(
        'CookingStatus', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Статус приготовления"
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.id} {self.date} {self.waiter} {self.status} {self.cooking_status}"


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, verbose_name="Заказ"
    )
    dish = models.ForeignKey(
        'menu.Menu', on_delete=models.CASCADE, verbose_name="Позиция"
    )
    quantity = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'

    def __str__(self):
        return f"{self.order} {self.dish} {self.quantity}"
