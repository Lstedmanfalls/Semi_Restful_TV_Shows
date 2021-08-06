from django.db import models
from django.db.models.fields import DateField

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"Shows: {self.id}, {self.title}, {self.network}, {self.release_date}, {self.description}"