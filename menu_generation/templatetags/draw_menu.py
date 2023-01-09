from django import template

from menu_generation.models import MenuItem


register = template.Library()


"""Фильтрация данных по статусу. Структурирование данных с многоуровневой вложенностью
для представления иерархии."""


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu_name: str) -> dict:
    objects = MenuItem.objects.filter(menu__name=menu_name, status="1")
    objects_dict = {}
    for object in objects:
        if object.parent is None:
            objects_dict[str(object.id)] = {"item": object, "subitems": []}
        else:
            objects_dict[str(object.parent_id)]["subitems"].append(object)

    result = {"menu_name": menu_name, "data": list(objects_dict.values())}
    print(result)
    return {"result": result}
