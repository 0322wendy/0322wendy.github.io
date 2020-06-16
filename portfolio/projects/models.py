from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, default='Project Title')
    # Images
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.summary
