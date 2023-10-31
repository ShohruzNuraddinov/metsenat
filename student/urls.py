from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudentListView.as_view()),
    path('<int:pk>/', views.StudentView.as_view()),
    path('add/', views.StudentCreateView.as_view()),

    path('sponsor/list/', views.StudentSponsorListView.as_view()),
    path('sponsor/add/', views.StudentSponsorAddView.as_view()),
    path('sponsor/<int:pk>/', views.StudentSponsorUpdateView.as_view()),

    path('transaction/', views.TransactionsView.as_view())
]
