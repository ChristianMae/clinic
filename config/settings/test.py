from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="iXnwnzt7RHPMNTKnnvh4EF0GDNsgdqNLn0Gol9wbV44P3w942l9lBHuXknPRGD24",
)

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"