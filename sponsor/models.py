from django.db import models
from utils.models import BaseModel


class SponsorChoices(models.TextChoices):
    new = "Yangi"
    moderation = "Moderatsiyada"
    approved = "Tasdiqlangan"
    canceled = "Bekor qilingan"


# Create your models here.
class Sponsor(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    used_amount = models.IntegerField(default=0)
    status = models.CharField(
        max_length=15, choices=SponsorChoices.choices, default=SponsorChoices.new
    )


class SponsorApplicationChoices(models.TextChoices):
    physical = "Jismoniy"
    legal = "Yuridik"


class SponsorApplication(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    type = models.CharField(
        max_length=15,
        choices=SponsorApplicationChoices.choices,
        default=SponsorApplicationChoices.physical,
    )

    company_name = models.CharField(max_length=255, null=True, blank=True)
