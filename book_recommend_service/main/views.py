from django.shortcuts import render
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_recommend_service.settings")# project_name project name
django.setup()
# Create your views here.


def home(request):
    return render(request, 'home.html')
