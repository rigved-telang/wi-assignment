from django.urls import path, include
from jobs import views

urlpatterns = [
    path('<pk>/', views.JobList.as_view()),
    path('<pk>/<job>/<act>/<n>', views.Act.as_view()),
]