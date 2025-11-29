from django.contrib.auth import get_user_model
from main.models import Feature
from django.core.management import call_command

def init_all():
    call_command('makemigrations')

    call_command('migrate', '--noinput')

    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@asif.me",
            password="asif@123"
        )

    Feature.objects.get_or_create(
        title="Clean UI",
        description="Simple and modern design for learning/testing"
    )
    Feature.objects.get_or_create(
        title="Extend Faster",
        description="Add APIs, frontend, authentication easily."
    )
