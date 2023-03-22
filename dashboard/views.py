from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from student.models import (
    Student
)
# Create your views here.
@login_required
def dashboard(request):
    students = Student.objects.all().order_by("-registration_id")[:5]
    context = {
        "students":students
    }
    return render(request, "dashboard.html", context)