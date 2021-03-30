from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class UserResume(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def get_user_personal_data(self):
        return PersonalData.objects.filter(user=self.user)
    
    def get_user_career_personal_data(self):
        return CareerObjective.objects.filter(user=self.user)
    
    def get_user_educational_background(self):
        return EducationBackground.objects.filter(user=self.user)
    
    def get_user_other_qualifications(self):
        return OtherQualification.objects.filter(user=self.user)
    
    def get_user_employment(self):
        return Employment.objects.filter(user=self.user)
    
    def get_user_skills(self):
        return Skills.objects.filter(user=self.user)
    
    def get_user_interest(self):
        return Interest.objects.filter(user=self.user)
    
    def get_user_reference(self):
        return References.objects.filter(user=self.user)
    
    def __str__(self):
        return self.user.username
    

class PersonalData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=256)
    id_no = models.CharField(max_length=12)
    address_code = models.IntegerField()
    adress_box = models.IntegerField()
    tel_no = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.user.username
    
class CareerObjective(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.user

class EducationBackground(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    done_date = models.DateTimeField()
    institution = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username

class OtherQualification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    done_date = models.DateTimeField()
    institution = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username
    
class Employment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    done_date = models.DateTimeField()
    responsibility = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    duties = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username
    
class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class References(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    work_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    tel_no = models.CharField(max_length=255)
    email = models.EmailField()
    town = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username