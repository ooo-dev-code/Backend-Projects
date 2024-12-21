from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Homework(models.Model):
    SUBJECTS = (
        ('Maths', 'Maths'),
        ('Physics', 'Physics'),
        ('Spanish', 'Spanish'),
        ('English', 'English'),
    )
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )
    subject = models.CharField(max_length=100, choices=SUBJECTS)
    due_date = models.CharField(max_length=100, choices=DAYS)
    content = models.TextField()
    
    class Meta:
        permissions = [
            ("is_teacher", "Can add homeworks to do"),
        ]

    def __str__(self):
        return self.subject
    
class Classes(models.Model):
    SUBJECTS = (
        ('Maths', 'Maths'),
        ('Physics', 'Physics'),
        ('Spanish', 'Spanish'),
        ('English', 'English'),
    )
    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )
    subject = models.CharField(max_length=100, choices=SUBJECTS)
    date = models.CharField(max_length=100, choices=DAYS)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        permissions = [
            ("is_office", "Can add classes to do"),
        ]

    def __str__(self):
        return self.subject