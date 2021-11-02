from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordsChangeView,Success_url_view
from django.contrib.auth import views as auth_views

urlpatterns = [
       path('register/', UserRegisterView.as_view(), name="register"),
       path('edit-profile/', UserEditView.as_view(), name="edit-profile"),
       #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name="change-password"),
       path('password/', PasswordsChangeView.as_view(), name="change-password"),
       path('password/success-url', Success_url_view, name="success-url"),
       
]