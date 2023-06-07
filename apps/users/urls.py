from django.urls import path
from apps.users.views import ResetPasswordAPIView

app_name = 'users'

urlpatterns = [
    # Остальные URL-шаблоны вашего приложения
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
]