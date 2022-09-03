import os
import joblib
from django.apps import AppConfig
from django.conf import settings
from input.params import model_name


class InterfaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'interface'
    MODEL_FILE = os.path.join(settings.MODELS, model_name)
    model = joblib.load(MODEL_FILE)