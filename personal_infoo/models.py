from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    desired_position = models.CharField(max_length=100)

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField()

class Education(models.Model):
    qualification = models.CharField(max_length=100)
    institution = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Project(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    technologies = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    description = models.TextField()
