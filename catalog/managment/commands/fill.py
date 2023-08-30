import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        def handle(self, *args, **options):
            Category.objects.all().delete()
            with open("data.json", "r", encoding='utf8') as file:
                categories = json.load(file)
                for category in categories:
                    name = category['fields']['title']
                    descr = category['fields']['description']
                    Category.objects.create(
                        title=name,
                        description=descr
                    )