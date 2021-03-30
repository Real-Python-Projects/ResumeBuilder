from django.contrib import admin
from .models import (
    PersonalData, CareerObjective, EducationBackground,
    OtherQualification, Employment, Skills,
    Interest, References, UserResume
)

# Register your models here.


class PersonalDataInLine(admin.StackedInline):
    model = PersonalData
    
class CareerObjectiveInline(admin.StackedInline):
    model = CareerObjective
    
class EducationBackgroundInline(admin.StackedInline):
    model = EducationBackground
    
class OtherQualificationsInline(admin.StackedInline):
    model = OtherQualification
    
class EmploymentInline(admin.StackedInline):
    model = Employment
    
class SkillsInline(admin.StackedInline):
    model = Skills
    
class InterestInline(admin.StackedInline):
    model = References
    
class UserResumeAdmin(admin.ModelAdmin):
    inlines = [PersonalDataInLine, CareerObjectiveInline, EducationBackgroundInline, 
               OtherQualificationsInline, EmploymentInline, SkillsInline, InterestInline]
    
admin.site.register(UserResume, UserResumeAdmin)

