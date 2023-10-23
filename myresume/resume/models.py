

from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    experience = models.TextField()
    education = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.lastname + ' ' + self.firstname


class University(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.CharField(max_length=30)
    date_end = models.CharField(max_length=30)
    faculty = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_start = models.CharField(max_length=30)
    date_end = models.CharField(max_length=30)
    description = models.TextField(null=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)

class Skills(models.Model):
    skillfulness = models.CharField(max_length=100)
    university_id = models.ForeignKey(Author, on_delete=models.CASCADE)