from django.db import models
from django.core.validators import MaxValueValidator


class Reference(models.Model):
    first_name = models.CharField(
        max_length=100,
        help_text="Введите имя с заглавной буквы",
        verbose_name="Имя"
    )
    patronymic = models.CharField(
        max_length=100,
        help_text="Введите отчество",
        verbose_name="Отчество",
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=100,
        help_text="Введите фамилию",
        verbose_name="Фамилия",
    )
    purpose = models.CharField(  # цель
        max_length=100,
        help_text="Введите цель выдачи справки",
        verbose_name="Цель выдачи справки",
    )
    quantity = models.PositiveIntegerField(
        validators=[MaxValueValidator(10)],
        help_text="Введите количество экземпляров справки",
        verbose_name="Количество экземпляров справки",
    )
    comment = models.CharField(
        max_length=255,
        help_text="Введите комментарий к справке",
        verbose_name="Комментарий к справке",
        null=True,
        blank=True,
    )
    date_of_changes = models.DateField(
        help_text="Введите дату изменения",
        verbose_name="Дaтa изменения",
        null=True,
        blank=True,
    )
