# Generated by Django 4.1.4 on 2023-01-03 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu_generation", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="menuitem",
            options={
                "ordering": ("name",),
                "verbose_name": "Элемент меню",
                "verbose_name_plural": "Элементы меню",
            },
        ),
    ]
