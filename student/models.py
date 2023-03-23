from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.urls import reverse
# Create your models here.

class Gender(models.TextChoices):
    MALE = "M", 'Male'
    FEMALE = "F", 'Female'
    OTHERS = "O", 'Others'

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="students_guarding/picture", null=True, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    email = models.EmailField(max_length=255, null=True, blank=True)
    temporary_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

class Student(Person):
    registration_id = models.PositiveBigIntegerField(null=True, blank=True)
    fathers_name = models.CharField(null=True, blank=True, max_length=255)
    mothers_name = models.CharField(null=True, blank=True, max_length=255)
    work_status = models.CharField(null=True, blank=True, max_length=255)
    disablity = models.BooleanField(default=False)
    disablity_description = models.CharField(max_length=255, null=True, blank=True)
    enrolled_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("student:student-detail", args=[self.id])

    


class StudentContact(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="phones")
    phone = PhoneNumberField()
    def __str__(self):
        return f"{self.student.first_name} {self.student.middle_name} {self.student.last_name}"



class Guardian(Person):
    phone = PhoneNumberField()
    identity = models.ImageField(upload_to="guardian/identity", blank=True, null=True)
    relationship = models.CharField(max_length=500, null=True, blank=True)
    