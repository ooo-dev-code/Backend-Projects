from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_, name='login'),
    path("logout/", LogoutView.as_view(next_page='frontpage'), name="logout"),
]
