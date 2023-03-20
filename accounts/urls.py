from django.urls import path, reverse_lazy

from django.contrib.auth.views import LogoutView

from accounts import views



app_name = 'accounts'

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("accounts:login")), name="logout"),
]