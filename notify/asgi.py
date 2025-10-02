import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notify.settings_docker_dev")

application = get_asgi_application()
