from django.db import models


# Create your models here.
class Job(models.Model):
    logo = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    industry = models.CharField(max_length=50)

    salary_from = models.PositiveIntegerField()
    salary_to = models.PositiveIntegerField()

    timing_from = models.TimeField()
    timing_to = models.TimeField()

    days_from = models.CharField(max_length=10)
    days_to = models.CharField(max_length=10)

    location = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.position} at {self.company}"


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Action(models.Model):
    job = models.ForeignKey(Job, null=True, on_delete=models.SET_NULL)
    candidate = models.ForeignKey(Candidate, null=True, on_delete=models.SET_NULL)
    actionType = models.CharField(max_length=5)

    def __str__(self):
        return self.actionType
