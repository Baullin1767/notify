import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notify.settings_docker_dev")

application = get_wsgi_application()
