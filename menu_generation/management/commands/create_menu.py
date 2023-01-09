from django.core.management.base import BaseCommand

from menu_generation.models import Menu, MenuItem


"""Заполнение тестовыми данными БД: Пункт меню №n -> Подпункт №n -> Подкатегория №1-3."""


class Command(BaseCommand):
    help = "Создание меню"

    def add_arguments(self, parser):
        parser.add_argument("creation", type=str)

    def handle(self, *args, **kwargs):
        for item in range(1, 6):
            menu = Menu.objects.create(name=f"Пункт меню №{item}")
            menu.save()
            self.stdout.write(self.style.SUCCESS(f"Пункт меню №{item} успешно добавлен"))
            self.generate_item(menu, item)

    def generate_item(self, menu: str, item: int):
        subitem = MenuItem.objects.create(name=f"Подпункт №{item}", menu=menu)
        self.stdout.write(self.style.SUCCESS(f"Подпункт №{item} успешно добавлен"))
        self.generate_item_list(subitem, menu)

    @staticmethod
    def generate_item_list(subitem: MenuItem, menu) -> list:
        subjects = MenuItem.objects.bulk_create(
            [
                MenuItem(name="Подкатегория №1", status="1", menu=menu, parent=subitem),
                MenuItem(name="Подкатегория №2", status="1", menu=menu, parent=subitem),
                MenuItem(name="Подкатегория №3", status="1", menu=menu, parent=subitem),
            ]
        )
        return subjects
