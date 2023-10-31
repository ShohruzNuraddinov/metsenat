from rest_framework import serializers

from . import models
from sponsor.serializers import SponsorSerailizer


class UniversitySerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.University
        fields = ['title']


class StudentSerializer(serializers.ModelSerializer):
    university = serializers.SlugRelatedField(
        slug_field='title',
        read_only=True,
        many=False
    )

    class Meta:
        model = models.Student
        fields = ['full_name', 'phone', 'university', 'study_type',
                  'required_amount', 'payed_amount', 'student_sponsor_url', 'created_at']


class StudentSponsorSerailizer(serializers.ModelSerializer):
    sponsor = serializers.SlugRelatedField(
        slug_field='full_name', many=False, read_only=True)
    student = serializers.SlugRelatedField(
        slug_field='full_name', many=False, read_only=True)

    class Meta:
        model = models.StudentSponsor
        fields = '__all__'


class StudentSponsorCreateSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentSponsor
        fields = ['id', 'student', 'sponsor', 'amount']


class StudentCreateSerailizer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = ['full_name', 'phone', 'university', 'study_type',
                  'required_amount', 'payed_amount']


class TransactionSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.SponsorTransactions
        fields = ['id', 'student', 'sponsor', 'amount']
