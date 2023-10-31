from django.db import models
from django.shortcuts import get_object_or_404
from sponsor.models import Sponsor


class StudyChoices(models.TextChoices):
    bakalavr = "Bakalavr"
    magistr = "Magistr"


class University(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


# Create your models here.
class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=15)

    university = models.ForeignKey(University, on_delete=models.CASCADE)
    study_type = models.CharField(max_length=15, choices=StudyChoices.choices)

    required_amount = models.IntegerField(default=0)
    payed_amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.full_name

    def student_sponsor_url(self):
        return f"/student/sponsor/list/?student_id={self.id}"


class SponsorTransactions(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    is_success = models.BooleanField(default=False)


class StudentSponsor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    class Meta:
        unique_together = ['student', 'sponsor']
