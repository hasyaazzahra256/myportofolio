from datetime import timedelta
from django.test import TestCase, Client
from django.utils import timezone
from main.models import Experience, Project 


class MainTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.now = timezone.now()

    def test_main_url_is_accessible(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-tidak-ada/")
        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        exp = Experience.objects.create(
            title="Asisten Laboratorium",
            description="Membantu praktikum mahasiswa.",
        )
        self.assertEqual(str(exp), "Asisten Laboratorium")

    def test_experience_page_accessible(self):
        response = self.client.get("/experience/")
        self.assertEqual(response.status_code, 200)

    def test_project_page_accessible_and_uses_correct_template(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")