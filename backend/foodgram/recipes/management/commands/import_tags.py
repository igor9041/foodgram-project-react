import csv

from django.core.management.base import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    help = 'Load ingredients data to DB'

    def handle(self, *args, **options):
        with open('data/tags.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                name, color, slug = row
                Tag.objects.get_or_create(
                    name=name, color=color, slug=slug
                )
                self.stdout.write(f'{name}, {color}, {slug}')
