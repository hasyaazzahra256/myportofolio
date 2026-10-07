import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from main.models import Experience, Project, Contact 
from main.forms import ProjectForm, ExperienceForm 

def is_editor(user):
    if not user or not user.is_authenticated:
        return False
    return user.groups.filter(name='Editor').exists()

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "npm": "2506617512",
        "study_program": "S1 Sistem Informasi",
        "bio": "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Indonesia.",
        "last_login": last_login,
        "is_editor": is_editor(request.user),
    }
    return render(request, "index.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Anda berhasil dibuat!')
            return redirect('main:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = redirect('main:show_main')
            response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return response
        else:
            messages.error(request, 'Username atau password salah!')
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "Anda telah berhasil keluar!")
    response = redirect('main:login')
    response.delete_cookie('last_login')
    return response

def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "title_query": title_query,
        "form": ExperienceForm(),
        "is_editor": is_editor(request.user),
    }
    return render(request, "experience.html", context)

@require_POST
def create_experience_ajax(request):
    if not (request.user.is_superuser or is_editor(request.user)):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio atau editor yang dapat menambahkan pengalaman."},
            status=403,
        )
    
    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required(login_url="/login/")
def create_experience(request):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

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

@login_required(login_url="/login/")
def edit_experience(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

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

@login_required(login_url="/login/")
def delete_experience(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect("main:show_experience")

def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for exp in experiences:
        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "description": exp.description,
                "start_date": exp.start_date or "",
                "ended_at": exp.ended_at or "",
                "thumbnail": exp.thumbnail or "",
                "is_ongoing": exp.is_ongoing,
            }
        })
        
    return JsonResponse(data, safe=False)

def show_project(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "title_query": title_query,
        "form": ProjectForm(),
        "is_editor": is_editor(request.user),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_project")
        
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "form": form
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def edit_project(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

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

@login_required(login_url="/login/")
def delete_project(request, id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=id)
    project.delete()
    return redirect("main:show_project")

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.stars.filter(id=request.user.id).exists():
        project.stars.remove(request.user)
        is_starred = False
    else:
        project.stars.add(request.user)
        is_starred = True

    return JsonResponse({
        'is_starred': is_starred,
        'total_stars': project.total_stars()
    })

@require_POST
def create_project_ajax(request):
    if not (request.user.is_superuser or is_editor(request.user)):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio atau editor yang dapat menambahkan proyek."},
            status=403,
        )
    
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('stars').all()
    
    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = list(project.stars.all())  # Konversi ke list python
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "thumbnail": project.thumbnail,
                "star_count": len(starred_users),  # Gunakan len() agar aman dan efisien
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        
    return JsonResponse(data, safe=False)

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contact_index.html", {"contacts": contacts})

def contact_add(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
        )
    contacts = Contact.objects.all()
    return render(request, "_contact_rows.html", {"contacts": contacts})

@require_http_methods(["DELETE"])
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponse("")

def contact_search(request):
    query = request.GET.get("q", "").strip()
    contacts = Contact.objects.filter(name__icontains=query) if query else Contact.objects.all()
    return render(request, "_contact_rows.html", {"contacts": contacts})

def create_admin_pws(request):
    if not User.objects.filter(username='hasya').exists():
        User.objects.create_superuser('hasya', 'hasyazahra25@gmail.com', 'Hasya2506@')
        return HttpResponse("Superuser 'hasya' berhasil dibuat di PWS! Password: Hasya2506@")
    else:
        u = User.objects.get(username='hasya')
        u.set_password('Hasya2506@')
        u.save()
        return HttpResponse("Password superuser 'hasya' berhasil di-reset menjadi Hasya2506@")