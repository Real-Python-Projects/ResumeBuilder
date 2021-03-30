from django.contrib import admin
from .models import (
    PersonalData, CareerObjective, EducationBackground,
    OtherQualification, Employment, Skills,
    Interest, References, UserResume
)

# Register your models here.
    
admin.site.register(UserResume)
