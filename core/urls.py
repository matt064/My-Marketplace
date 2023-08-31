from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("item/", include('item.urls')),

    path("singup/", views.singup, name="singup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
    path('logout/', views.logoutPage, name="logout"),
]