from django.urls import path
from django.contrib.auth import views as auth_views

from account.forms import LoginForm
from .views import RegisterView, TrainLoginView
from . import views


urlpatterns = [
   path('register/', RegisterView.as_view(), name='account-register'),
#    path('login/', TrainLoginView.as_view(template_name = "account/login.html"), name='account-login'),
   path('login/', TrainLoginView.as_view(redirect_authenticated_user = True, 
                                        template_name = 'account/login.html', 
                                        authentication_form = LoginForm),
                                        name = 'account-login'
    ),
    path('logout/', auth_views.LogoutView.as_view(template_name = "account/logout.html"), name='account-logout'),
]