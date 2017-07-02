from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    # Menu and header layout - horizontal or vertical
    layout = 'vertical'

class BlogConfig(AppConfig):
    name = 'blog'
