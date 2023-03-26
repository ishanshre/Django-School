from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

from student.models import Student
from student.form import StudentCreateForm, StudentUpdateForm, StudentDeleteForm
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


class StudentDetailView(LoginRequiredMixin, View):
    template_name = "student/student_detail.html"
    def get(self, request, *args, **kwargs):
        student_id = self.kwargs['pk']
        student = get_object_or_404(Student, id=student_id)
        student_update = StudentUpdateForm(instance=student)
        student_delete = StudentDeleteForm()
        context = {
            "student":student,
            "student_update": student_update,
            "student_delete": student_delete,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        student_id = self.kwargs['pk']
        student = get_object_or_404(Student, id=student_id)
        student_update = StudentUpdateForm(instance=student)
        student_delete = StudentDeleteForm()
        if 'update' in request.POST:
            student_update = StudentUpdateForm(request.POST, request.FILES, instance=student)
            if student_update.is_valid():
                student_update.save()
                messages.success(request, 'Student Updated')
                return redirect("student:student-detail", pk=student_id)
        if 'delete' in request.POST:
            student_delete = StudentDeleteForm(request.POST)
            print("delete jot")
            if student_delete.is_valid():
                print('detele hit')
                student.delete()
                messages.success(request, 'Student Deleted')
                return redirect("student:student-manage")
        context = {
            "student":student,
            "student_update": student_update,
            "student_delete": student_delete,
        }
        return render(request, self.template_name, context)