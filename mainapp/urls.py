from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('', ResumeView, name='resume'),
    path('generate/', GeneratePdf, name='generate-pdf'),
    
    path('form-title/', CreateResumeView, name='create-resume'),
    path('create-personal-data/', CreatePDataView, name='create-personal-data'),
    path('create-career/', CreateCareerObjectiveView, name='create-career'),

]
