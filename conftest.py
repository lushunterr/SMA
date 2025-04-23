import os
import sys
import django
from django.conf import settings

def pytest_configure():
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SMA.settings')
    django.setup()

# Solo una prueba para verificar que el entorno de Django se carga correctamente