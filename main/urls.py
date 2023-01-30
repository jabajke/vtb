from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('geographical/', geographical, name='geographical'),
    path('economic/', economic_dev, name='economic'),
    path('export/', export, name='export'),
    path('nature/', nature, name='nature'),
    path('ecological/', ecological, name='ecological'),
    path('biography/', biography, name='biography'),
    path('short_history/', short_history, name='short_history'),
    path('memory/', memory, name='memory')

]
