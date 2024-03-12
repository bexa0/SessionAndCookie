from django.urls import path
from app_hw.views import *

urlpatterns = [
    path('', start_view, name='main'),
]
