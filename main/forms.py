from django import forms
from main.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "category", "project_url"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Judul Proyek"}),
            "description": forms.Textarea(attrs={"placeholder": "Deskripsi Proyek", "rows": 4}),
            "category": forms.TextInput(attrs={"placeholder": "Kategori Proyek"}),
            "project_url": forms.URLInput(attrs={"placeholder": "https://..."}),
        }