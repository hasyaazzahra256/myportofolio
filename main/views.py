from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from main.models import Experience, Project  

def show_main(request):
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "npm": "2506617512",
        "study_program": "S1 Sistem Informasi",
        "bio": "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Indonesia.",
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)

def create_admin_pws(request):
    if not User.objects.filter(username='hasya').exists():
        User.objects.create_superuser('hasya', 'hasyazahra25@gmail.com', 'Hasya2506@')
        return HttpResponse("Superuser 'hasya' berhasil dibuat di PWS! Password: Hasya2506@")
    else:
        u = User.objects.get(username='hasya')
        u.set_password('Hasya2506@')
        u.save()
        return HttpResponse("Password superuser 'hasya' berhasil di-reset menjadi Hasya2506@")