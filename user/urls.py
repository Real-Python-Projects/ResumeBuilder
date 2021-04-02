from django.urls import path
from .views import (RegisterView, LogInView, LogOutView, RequestResetEmail,
                    VerificationView)

app_name = 'user'

urlpatterns = [
    path('login/',LogInView, name='login'),
    path('logout/', LogOutView, name="logout"),
    path('register/', RegisterView, name='register'),
    path('reset-email/', RequestResetEmail, name='reset-email'),
    path('activate/<uidb64>/<token>/', VerificationView, name='activate'),
    path('request-reset-email/', RequestResetEmail, name="request-reset-email"),
]


