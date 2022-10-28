from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import SignUp

app_name = 'users'


urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(
            template_name='users/logout.html'
        ),
        name='logout'
    ),
    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
    ),
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html'
        ),
        name='login'
    )
]
