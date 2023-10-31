from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from utils.paginations import StandartResultPagination
from .models import Student, StudentSponsor, SponsorTransactions
from sponsor.models import Sponsor
from .serializers import StudentSerializer, StudentCreateSerailizer, StudentSponsorSerailizer, StudentSponsorCreateSerailizer, TransactionSerailizer

# Create your views here.


class StudentListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    pagination_class = StandartResultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['study_type', 'university']


class StudentCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerailizer


class StudentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerailizer


class StudentSponsorAddView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorCreateSerailizer

    def create(self, request):
        amount = int(request.POST.get('amount'))
        student_id = int(request.POST.get('student'))
        sponsor_id = int(request.POST.get('sponsor'))

        student = Student.objects.get(id=student_id)
        sponsor = Sponsor.objects.get(id=sponsor_id)

        res = {
            'student': student.id,
            'sponsor': sponsor.id,
            'amount': amount,
        }

        student_sponsor = StudentSponsor.objects.filter(
            student=student, sponsor=sponsor)

        if not student_sponsor.exists():
            print(sponsor.amount, amount)
            if sponsor.amount >= amount:
                if student.payed_amount < student.required_amount:
                    if (student.payed_amount + amount) <= student.required_amount:
                        sponsor.amount -= amount
                        sponsor.used_amount += amount
                        sponsor.save()

                        student.payed_amount += amount
                        student.save()
                        SponsorTransactions.objects.create(
                            sponsor=sponsor, student=student, amount=amount, is_success=True)

                        StudentSponsor.objects.create(
                            student=student, sponsor=sponsor, amount=amount)
                        res['message'] = "Success Added"
                        return Response(res)
                    else:
                        res['message'] = "Amount has increased"
                        return Response(res)
                return Response('Amount will exceed')
            res['message'] = "Amount is not enough"
            return Response(res)
        else:
            res['message'] = "Already Added!"
            return Response(res)


class StudentSponsorUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorCreateSerailizer


class StudentSponsorListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerailizer

    def get_queryset(self):
        queryset = StudentSponsor.objects.all()
        student_id = self.request.query_params.get('student_id')
        if student_id is not None:
            queryset = queryset.filter(student__id=student_id)
        return queryset


class TransactionsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = SponsorTransactions.objects.all()
    serializer_class = TransactionSerailizer
