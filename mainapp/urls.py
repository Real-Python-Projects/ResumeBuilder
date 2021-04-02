from django.urls import path
from .views import GeneratePdf, ResumeView

app_name = 'mainapp'

urlpatterns = [
    path('', ResumeView, name='resume'),
    path('generate/', GeneratePdf, name='generate-pdf'),

]
