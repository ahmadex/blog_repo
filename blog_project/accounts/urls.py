from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserCreateView.as_view(), name='register'),
    path('register/<str:pk>/',views.UserCreateView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='gettoken'),
    path('update/<str:pk>/',views.UserCreateView.as_view(), name='update'),
    path('delete/<str:pk>/',views.UserCreateView.as_view(), name='delete'),
    path('login/',TokenObtainPairView, name='login'),
    path('refresh_token/', TokenRefreshView, name='refresh_token'),
    path('veirfy_token/', TokenVerifyView, name='token_verify')
]