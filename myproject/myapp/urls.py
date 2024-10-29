from django.urls import path
from . import views

urlpatterns = [
    path('', views.customize_news, name='customize_news'),
]