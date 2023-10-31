from rest_framework import serializers

from .models import Sponsor, SponsorApplication


class SponsorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class SponsorApplicationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = SponsorApplication
        fields = '__all__'
