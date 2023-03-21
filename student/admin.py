from django.contrib import admin

# Register your models here.
from student.models import Student, Guardian, StudentContact

# admin.site.register(Student)
admin.site.register(Guardian)

class StudentContactInline(admin.StackedInline):
    model = StudentContact
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentContactInline]

