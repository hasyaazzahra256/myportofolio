from django.urls import path
from main.views import show_main, show_experience, show_project, create_project, delete_project, get_projects_json, create_admin_pws

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('experience/', show_experience, name='show_experience'),
    path('projects/', show_project, name='show_project'),
    path("projects/add/", create_project, name="create_project"),
    path("projects/delete/<uuid:id>/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path('create-admin-pws/', create_admin_pws, name='create_admin_pws'),
]