from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name=""),
    path("homepage", views.homepage.as_view(), name="homepage"),
    path("loggedin", views.loggedin.as_view(), name="loggedin"),
    path("login", views.loginview.as_view(), name ="login"),
    path("logincomplete", views.logincomplete, name="logincomplete"),
    path("signup", views.signupview.as_view(), name="signup"),
    path("signupcomplete", views.signupcomplete, name="signupcomplete"),
    path("formcomplete", views.formcomplete, name="formcomplete"),
]