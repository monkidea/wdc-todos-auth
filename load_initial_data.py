import django


def main():
    django.setup()

    from todos_app.models import Todo
    from django.contrib.auth.models import User
    admin = User.objects.create_superuser(
        username='admin', email='admin@example.com', password='admin')

    ADMIN_TASKS = [
        ('Send update email to board', True),
        ('Release staging version', False),
        ('Review sprint next week', False),
    ]
    for title, completed in ADMIN_TASKS:
        Todo.objects.create(
            title=title, completed=completed, owner=admin)

    user2 = User.objects.create_superuser(
        username='user2', email='user2@example.com', password='user2')
    Todo.objects.create(
        title="My only todo", owner=user2)

if __name__ == '__main__':
    main()
