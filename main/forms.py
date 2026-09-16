from django import forms
from main.models import Project

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