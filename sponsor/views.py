from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import pagination, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utils.paginations import StandartResultPagination

from .models import Sponsor, SponsorApplication
from .serializers import SponsorSerailizer, SponsorApplicationSerailizer
# Create your views here.


class SponsorList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    pagination_class = StandartResultPagination
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerailizer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['amount', 'created_at', 'status']


class SponsorCreateView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    pagination_class = StandartResultPagination
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerailizer


class SponsorView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerailizer


# class SponsorApplicationView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]

#     queryset = SponsorApplication.objects.all()
#     serializer_class = SponsorApplicationSerailizer
#     pagination_class = StandartResultPagination


# class SponsorAplicationCreateView(generics.CreateAPIView):
#     queryset = SponsorApplication.objects.all()
#     serializer_class = SponsorApplicationSerailizer
