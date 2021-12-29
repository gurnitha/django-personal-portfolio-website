# user_interface/models.py

# Djang modules
from django.db import models
from django.contrib.auth.models import AbstractUser

# Locals

# Create your models here.

# Model: User
class User(AbstractUser):
	pass


# Model: InformationModel
class InformationModel(models.Model):
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    # avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    CV = models.FileField(upload_to="cv/", blank=True, null=True)
    fewWords = models.CharField(max_length=500, blank=True, null=True)

    #Social Networks
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    other = models.URLField(blank=True, null=True)

    def save(self, **kwargs):
        if kwargs.__contains__('request') and self.user is None:
            request = kwargs.pop('request')
            self.user = request.user
        super(InformationModel, self).save(**kwargs)

    def __str__(self):
        return self.firstName


# Model: EducationModel
class EducationModel(models.Model):
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    the_year = models.CharField(max_length=50, blank=True, null=True)
    institute = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-the_year']

    def save(self, **kwargs):
        if kwargs.__contains__('request') and self.user is None:
            request = kwargs.pop('request')
            self.user = request.user
        super(EducationModel, self).save(**kwargs)