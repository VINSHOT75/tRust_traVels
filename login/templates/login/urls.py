from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path("ngofeed/", views.home, name="ngohome"),
path("",views.logmein ,name="login"),
path("signup/",views.signup ,name = "signup"),
path("logout/",views.logout ,name = "signup"),
path("password_reset/",auth_views.PasswordResetView.as_view(template_name='ngo/password_reset.html'),name="password_reset"),
path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(template_name='ngo/password_reset_done.html'),name="password_reset_done"),
path("password_reset_confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='ngo/password_reset_confirm.html'),name="password_reset_confirm"),
path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(template_name='ngo/password_reset_complete.html'),name="password_reset_complete"),
]