from django.urls import path

from student import views

app_name="student"

urlpatterns = [
    path("", views.StudentManageView.as_view(), name="student-manage"),
    path("<int:pk>/detail", views.StudentDetailView.as_view(), name="student-detail"),
    path("<int:pk>/<int:student_pk>/guardian/update/", views.GuardianUpdateView.as_view(), name='guardian_update'),
    path("<int:pk>/<int:student_pk>/guardian/delete/", views.GuardianDeleteView.as_view(), name='guardian_delete'),
]