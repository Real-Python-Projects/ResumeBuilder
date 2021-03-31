from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
User = get_user_model()
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.user.username
    