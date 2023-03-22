from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.messages import success

from django.contrib.auth.mixins import LoginRequiredMixin

from student.models import Student
# Create your views here.

class StudentList(LoginRequiredMixin, ListView):
    template_name = "student/student_list.html"
    model = Student
    context_object_name = "students"
    def get_queryset(self):
        return Student.objects.all().order_by("-enrolled_date")

