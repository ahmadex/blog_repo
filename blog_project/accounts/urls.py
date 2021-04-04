from django.urls import path, include
from accounts import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserCreateView.as_view(), name='register'),
    path('register/<str:pk>/',views.UserCreateView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='gettoken'),
    path('update/<str:pk>/',views.UserCreateView.as_view(), name='update'),
    path('delete/<str:pk>/',views.UserCreateView.as_view(), name='delete'),
    path('login/',TokenObtainPairView, name='login'),
    path('refresh_token/', TokenRefreshView, name='refresh_token'),
    path('veirfy_token/', TokenVerifyView, name='token_verify'),
    path('my_login/', TemplateView.as_view(template_name='accounts/login.html')),
    path('social_accounts/', include('allauth.urls')),

]