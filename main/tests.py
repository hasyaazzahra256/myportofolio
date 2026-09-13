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
            category="ORGANIZATION",
            thumbnail="https://example.com/thumb.png",
            started_at=self.now,
            ended_at=self.now + timedelta(days=30),
        )
        self.assertEqual(str(exp), "Asisten Laboratorium")

    def test_experience_page(self):
        Experience.objects.create(
            title="Proyek Django",
            description="Membuat aplikasi web portofolio.",
            category="PROJECT",
            thumbnail="https://example.com/django.png",
            started_at=self.now,
            ended_at=self.now + timedelta(days=10),
        )
        response = self.client.get("/experience/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Proyek Django")

    def test_empty_experience_page(self):
        response = self.client.get("/experience/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada pengalaman")

    def test_completed_experience(self):
        past_start = self.now - timedelta(days=60)
        past_end = self.now - timedelta(days=30)
        exp = Experience.objects.create(
            title="Magang Selesai",
            description="Magang musim panas.",
            category="WORK",
            thumbnail="https://example.com/work.png",
            started_at=past_start,
            ended_at=past_end,
        )
        self.assertFalse(exp.is_ongoing)

    def test_project_page_accessible_and_uses_correct_template(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")

    def test_project_page_shows_data(self):
        Project.objects.create(
            title="Aplikasi Portofolio",
            description="Membuat web portofolio dengan Django.",
            technology="Django & Tailwind",
            project_url="https://github.com"
        )
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aplikasi Portofolio")

    def test_empty_project_page(self):
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada proyek")