from django.shortcuts import render

from student.models import (
    Student
)
# Create your views here.
def dashboard(request):
    students = Student.objects.all().order_by("-registration_id")[:5]
    context = {
        "students":students
    }
    return render(request, "dashboard.html", context)