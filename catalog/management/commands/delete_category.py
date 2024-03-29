from django.core.management.base import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    """ Удаляет данные из таблицы категорий. """

    def handle(self, *args, **kwargs) -> None:
        try:
            Category.objects.all().delete()
        except Exception as e:
            print(f'Не удалось удалить данные из таблицы категорий. '
                  f'Ошибка {str(e)}.')
