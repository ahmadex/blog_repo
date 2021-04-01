from django.urls import path
from blog_app import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = 'blog'

urlpatterns = [
    path('home/',views.BlogView.as_view(),name='blog'),
    path('home/<str:pk>/',views.BlogView.as_view(),name='blog_detail'),
    path('blog_create/',views.BlogView.as_view(),name='blog_create'),
    path('blog_update/<str:pk>/',views.BlogView.as_view(),name='blog_create'),
    path('blog_delete/<str:pk>/',views.BlogView.as_view(),name='blog_create'),

    # path('login/',TokenObtainPairView.as_view(), name='login'),
    # path('refresh/',TokenRefreshView.as_view(), name='refresh')

]