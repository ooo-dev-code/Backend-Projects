from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("homework/", views.homework, name="homework"),
    path("create_homework/", views.create_homework, name="create_homework"),
    path("add_class/", views.add_class, name="add_class"),
    path("classes/", views.classes, name="classes"),
    path("logout/", LogoutView.as_view(next_page='frontpage'), name="logout"),
]
