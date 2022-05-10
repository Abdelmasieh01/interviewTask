from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150, unique=True)
    
    CHOICES = [
        ('dr', 'Draft'),
        ('ac', 'Active'),
        ('dn', 'Done'),
        ('ar', 'Archived'),
    ]

    state = models.CharField(max_length=2, choices=CHOICES, default='dr')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title