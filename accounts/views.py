from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from accounts.forms import LoginForm
# Create your views here.

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = "auth/login.html"
    success_url = reverse_lazy("student:dashboard")

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("student:dashboard")
        return super().dispatch(request, *args, **kwargs)
