from django.db import models
from datetime import date

class ShowsManager(models.Manager):
    def create_validator(self, postData):
        today = date.today()
        existing_shows = Shows.objects.filter(title = postData['title'])
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        elif str(today) < postData['release_date']:
            errors["release_date"] = "Release date cannot be now or in the future"
        if len(postData["description"]) !=0 and len(postData['description']) < 10:
            errors["description"] = "Description can be blank or at least 10 characters"
        elif len(existing_shows) > 0:
            errors["duplicate"] = "That show already exists"
        return errors

    def update_validator(self, postData):
        today = date.today()
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        elif str(today) < postData['release_date']:
            errors["release_date"] = "Release date cannot be now or in the future"
        if len(postData["description"]) !=0 and len(postData['description']) < 10:
            errors["description"] = "Description can be blank or at least 10 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
    def __repr__(self):
        return f"Shows: {self.id}, {self.title}, {self.network}, {self.release_date}, {self.description}"