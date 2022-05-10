from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150, unique=True)
    
    draft = 0
    active = 1
    done = 2
    archived = 3
    CHOICES = [
        (draft, 'Draft'),
        (active, 'Active'),
        (done, 'Done'),
        (archived, 'Archived'),
    ]

    state = models.IntegerField(choices=CHOICES, default=draft)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title