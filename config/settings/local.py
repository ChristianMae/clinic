from .base import *  # noqa
from .base import env


DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="^#lg4cilg8(ec4t_nj4(p(2&#(&@c5_75m2!4mu_0zwa3&+aq^",
)

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"] 

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}