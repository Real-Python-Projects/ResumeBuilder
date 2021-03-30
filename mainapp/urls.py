from django.urls import path
from .views import GeneratePdf, ResumeView

app_name = 'mainapp'

urlpatterns = [
    path('generate/', GeneratePdf, name='generate-pdf'),
    path('resume/', ResumeView, name='resume' ),
]
