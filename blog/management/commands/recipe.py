from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        Post.objects.create(author='', image='', title='', desc='')