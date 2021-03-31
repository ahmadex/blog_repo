from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserCreateView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='gettoken'),
    path('refresh_token/', TokenRefreshView, name='refresh_token'),
    path('veirfy_token/', TokenVerifyView, name='token_verify')
]