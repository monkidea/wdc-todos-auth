from django.core.management.base import BaseCommand, CommandError
from todos_app.models import Todo


class Command(BaseCommand):
    help = 'Create a new Todo from the command line'

    def add_arguments(self, parser):
        parser.add_argument(
            '-t', '--title', help="The title of your TODO",
            required=True)

    def handle(self, *args, **options):
        # In:
        title = options['title']

        # Process / main:
        todo = Todo.objects.create(title=title)

        # Out:
        self.stdout.write("Todo created. Id is: {}".format(todo.id))
