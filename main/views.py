import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from main.models import Experience, Project  
from main.forms import ProjectForm, ExperienceForm 

def show_main(request):
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "npm": "2506617512",
        "study_program": "S1 Sistem Informasi",
        "bio": "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Indonesia.",
    }
    return render(request, "index.html", context)

def show_experience(request):
    # 1. serialisasi data Experience dari DB ke JSON
    data = serializers.serialize('json', Experience.objects.all())
    
    # 2. deserialisasi balik ke Python list/dict
    exp_json = json.loads(data)
    
    # 3. ambil isi 'fields' dan sisipkan 'id' (pk)
    experience_list = []
    for item in exp_json:
        exp_data = item['fields']
        exp_data['id'] = item['pk']
        experience_list.append(exp_data)

    context = {
        "name": "Hasya Azzahra Rangkuti",
        "experience_list": experience_list,
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")
        
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "form": form,
        "title_page": "Tambah Experience Baru"
    }
    return render(request, "experience_form.html", context)

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_experience")

    context = {
        "name": "Hasya Azzahra Rangkuti",
        "form": form,
        "experience": experience,
        "title_page": "Edit Experience"
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect("main:show_experience")

def get_experiences_json(request):
    experiences = Experience.objects.all()
    exp_json = serializers.serialize("json", experiences)
    return HttpResponse(exp_json, content_type="application/json")

def show_project(request):
    # 1. tangkap parameter pencarian dari query string URL (?title=...)
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    # 2. filter proyek berdasarkan judul jika ada kata kunci pencarian
    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # 3. serialisasi data Project dari database ke format JSON
    data = serializers.serialize('json', projects)
    
    # 4. deserialisasi dari string JSON ke daftar dictionary Python
    projects_json = json.loads(data)
    
    # 5. ambil isi 'fields' dan sisipkan 'id' (pk)
    project_list = []
    for item in projects_json:
        project_data = item['fields']
        project_data['id'] = item['pk']
        project_list.append(project_data)

    context = {
        "name": "Hasya Azzahra Rangkuti",
        "project_list": project_list,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_project")
        
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "form": form
    }
    return render(request, "projects_form.html", context)

def edit_project(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_project")

    context = {
        "name": "Hasya Azzahra Rangkuti",
        "form": form,
        "project": project,
    }
    return render(request, "projects_form.html", context)

def delete_project(request, id):
    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect("main:show_project")

def create_admin_pws(request):
    if not User.objects.filter(username='hasya').exists():
        User.objects.create_superuser('hasya', 'hasyazahra25@gmail.com', 'Hasya2506@')
        return HttpResponse("Superuser 'hasya' berhasil dibuat di PWS! Password: Hasya2506@")
    else:
        u = User.objects.get(username='hasya')
        u.set_password('Hasya2506@')
        u.save()
        return HttpResponse("Password superuser 'hasya' berhasil di-reset menjadi Hasya2506@")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    
    if title_query:
        projects = projects.filter(title__icontains=title_query)
        
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")