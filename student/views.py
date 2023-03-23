from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from student.models import Student
from student.form import StudentCreateForm
# Create your views here.

class StudentManageView(LoginRequiredMixin, View):
    template_name = "student/student_list.html"
    def get(self, request, *args, **kwargs):
        students = Student.objects.all().order_by("-created_date")
        student_create = StudentCreateForm()
        context = {
            "students":students,
            "student_create":student_create,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        students = Student.objects.all().order_by("-created_date")
        student_create = StudentCreateForm()
        if "create" in request.POST:
            student_create = StudentCreateForm(request.POST, request.FILES)
            if student_create.is_valid():
                student_create.save()
                messages.success(request, 'Student Added Successfully')
                return redirect("dashboard:dashboard")
                
        context = {
            "students":students,
            "student_create":student_create,
        }
        return render(request, self.template_name, context)
