from django.db import models
from django.conf import settings


class Shift(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Дата")
    start_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Время")
    end_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Время")

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return f"{self.date} {self.start_time} {self.end_time}"


class ShiftUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    shift = models.ForeignKey(
        'Shift', on_delete=models.CASCADE, verbose_name="Смена"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self):
        return f"{self.shift} {self.user}"
