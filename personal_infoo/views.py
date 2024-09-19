from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import PersonalInfo, WorkExperience, Education, Skill, Project

def portfolio_view(request):
    personal_info = PersonalInfo.objects.first()
    work_experiences = WorkExperience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        'personal_info': personal_info,
        'work_experiences': work_experiences,
        'education': education,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'portfolio.html', context)
