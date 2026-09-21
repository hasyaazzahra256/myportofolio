from django.urls import path
from main.views import (
    show_main, show_experience, create_experience, edit_experience, delete_experience, get_experiences_json,
    show_project, create_project, edit_project, delete_project, get_projects_json, register, login_user, logout_user,
    create_admin_pws
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path("logout/", logout_user, name="logout"),

    
    # experience URLs
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"), # Gunakan <int:id> jika primary key bertipe integer
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),

    # project URLs
    path("projects/", show_project, name="show_project"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:id>/edit/", edit_project, name="edit_project"),
    path("projects/<uuid:id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),

    # admin PWS Helper
    path("create-admin-pws/", create_admin_pws, name="create_admin_pws"),

    path('register/', register, name='register'),

    path('login/', login_user, name='login'),
]