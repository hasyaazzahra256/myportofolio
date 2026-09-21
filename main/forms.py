from django import forms
from main.models import Project, Experience

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tech_stack", "project_url", "thumbnail"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Portfolio Website"}),
            "description": forms.Textarea(attrs={"placeholder": "Ceritakan Proyekmu", "rows": 4}),
            "tech_stack": forms.TextInput(attrs={"placeholder": "Django, Python, HTML, CSS"}),
            "project_url": forms.URLInput(attrs={"placeholder": "https://..."}),
            "thumbnail": forms.URLInput(attrs={"placeholder": "https://..."}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "start_date", "ended_at", "thumbnail"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Judul Posisi/Peran", "style": "width: 100%; padding: 0.6rem; border: 1px solid #ccc; border-radius: 4px;"}),
            "description": forms.Textarea(attrs={"placeholder": "Deskripsi Pekerjaan/Tanggung Jawab", "rows": 4, "style": "width: 100%; padding: 0.6rem; border: 1px solid #ccc; border-radius: 4px;"}),
            "start_date": forms.TextInput(attrs={"placeholder": "Bulan/Tahun Mulai (misal: Jan 2025)", "style": "width: 100%; padding: 0.6rem; border: 1px solid #ccc; border-radius: 4px;"}),
            "ended_at": forms.TextInput(attrs={"placeholder": "Bulan/Tahun Selesai / Present", "style": "width: 100%; padding: 0.6rem; border: 1px solid #ccc; border-radius: 4px;"}),
            "thumbnail": forms.URLInput(attrs={"placeholder": "https://link-gambar-thumbnail.com/image.png", "style": "width: 100%; padding: 0.6rem; border: 1px solid #ccc; border-radius: 4px;"}),
        }