from django.urls import path
from blog_app import views


app_name = 'blog'

urlpatterns = [
    path('blog_list/',views.BlogList.as_view(),name='blog_list'),
    path('blog_list/<str:pk>/',views.BlogList.as_view(),name='blog_detail'),
    path('blog_create/',views.BlogView.as_view(),name='blog_create'),
    path('blog_update/<str:pk>/',views.BlogView.as_view(),name='blog_create'),
    path('blog_publish/<str:pk>/',views.BlogPublish.as_view(),name='blog_publish'),
    path('blog_delete/<str:pk>/',views.BlogView.as_view(),name='blog_create'),
]