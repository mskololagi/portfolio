from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PersonalInfo, WorkExperience, Education, Skill, Project

admin.site.register(PersonalInfo)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
