from django.db import models


CHOICES_STATUS = [
    ("1", "Доступно"),
    ("0", "Недоступно"),
]


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    status = models.CharField(
        max_length=10,
        verbose_name="Cтатус",
        choices=CHOICES_STATUS,
        default=CHOICES_STATUS[0][0],
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name="Меню",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Родитель",
        related_name="Наследник",
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    status = models.CharField(
        max_length=100,
        verbose_name="Статус",
        choices=CHOICES_STATUS,
        default=CHOICES_STATUS[0][0],
    )
    url = models.SlugField(
        verbose_name="URL",
        help_text="Подключение элемента через URL",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("menu__id", "-parent__id", "name")
        verbose_name = "Элемент меню"
        verbose_name_plural = "Элементы меню"

    def get_absolute_url(self):
        return "/%s" % self.url

    def __str__(self):
        return self.name
