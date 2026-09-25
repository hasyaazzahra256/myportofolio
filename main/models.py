import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    start_date = models.CharField(max_length=50, blank=True, null=True)
    ended_at = models.CharField(max_length=50, blank=True, null=True)
    is_ongoing = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=100, blank=True, null=True)
    tech_stack = models.CharField(max_length=255, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True) 

    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )

    def __str__(self):
        return self.title