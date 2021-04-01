from django.urls import path
from .views import RegisterView

app_name = 'user'

urlpatterns = [
    path('register/',RegisterView, name='regidter')
]


