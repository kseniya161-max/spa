import pytest
import os
from django.conf import settings

@pytest.fixture(scope='session', autouse=True)
def configure_django():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
    import django
    django.setup()
