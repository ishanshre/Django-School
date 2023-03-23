from django.urls import path

from student import views

app_name="student"

urlpatterns = [
    path("", views.StudentManageView.as_view(), name="student-manage"),
    path("<int:pk>/detail", views.StudentDetailView.as_view(), name="student-detail"),
]