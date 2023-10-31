from django.urls import path

from . import views

urlpatterns = [
    path('', views.SponsorList.as_view()),
    path('<int:pk>/', views.SponsorView.as_view()),
    path('add/', views.SponsorCreateView.as_view()),
    # path('application/', views.SponsorApplicationView.as_view()),
    # path('application/add/', views.SponsorAplicationCreateView.as_view())
]
