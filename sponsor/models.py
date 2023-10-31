from django.db import models


class SponsorChoices(models.TextChoices):
    not_confirmed = 'Tasdiqlanmagan'
    new = "Yangi"
    moderation = "Moderatsiyada"
    approved = "Tasdiqlangan"
    canceled = "Bekor qilingan"


# Create your models here.
class Sponsor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    used_amount = models.IntegerField(default=0)
    status = models.CharField(
        max_length=15, choices=SponsorChoices.choices, default=SponsorChoices.not_confirmed
    )
    company_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name


class SponsorApplicationChoices(models.TextChoices):
    physical = "Jismoniy"
    legal = "Yuridik"


class SponsorApplication(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField(default=0)
    type = models.CharField(
        max_length=15,
        choices=SponsorApplicationChoices.choices,
        default=SponsorApplicationChoices.physical,
    )

    company_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name
