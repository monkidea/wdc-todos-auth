from django.core.management.base import BaseCommand, CommandError
from todos_app.models import Todo


class Command(BaseCommand):
    help = 'Create a new Todo from the command line'

    def add_arguments(self, parser):
        parser.add_argument(
            '--id', help="The ID of your TODO", type=int,
            required=True)

    def handle(self, *args, **options):
        # In:
        todo_id = options['id']
        print(todo_id)

        # Process / main:
        todo = Todo.objects.get(id=todo_id)
        todo.completed = not todo.completed

        todo.save()

        new_state = 'PENDING'
        if todo.completed:
            new_state = 'DONE'

        # Out:
        self.stdout.write("Todo is now {}".format(new_state))
