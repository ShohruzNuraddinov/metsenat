from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated

from student.models import Student
from sponsor.models import Sponsor
# Create your views here.


class HomePageView(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payed_amount = 0
        required_amount = 0
        student_data = {}
        sponsor_data = {}
        for month in range(1, 13):
            students = Student.objects.filter(created_at__month=month).count()
            sponsors = Sponsor.objects.filter(created_at__month=month).count()
            student_data[str(month)] = students
            sponsor_data[str(month)] = sponsors

        for sponsor in Sponsor.objects.all():
            payed_amount += sponsor.amount

        for student in Student.objects.all():
            required_amount += student.required_amount

        res = {
            'student_graph': student_data,
            'sponsor_graph': sponsor_data,
            'payed_amount': payed_amount,
            'required_amount': required_amount
        }
        return Response(res)
