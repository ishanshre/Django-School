from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm

from accounts.models import Profile
# Register your models here.

User = get_user_model()

class ProfileInline(admin.StackedInline):
    model = Profile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {
            "fields":("date_of_birth",)
        }),
    )
    add_fieldsets = (
        ("Create User", {
            "classes": ("wide",),
            "fields":("username","email","password1","password2"),
        }),
    )

    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileInline]
        return []