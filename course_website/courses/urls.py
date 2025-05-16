from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='courses/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='course_list'), name='logout'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:pk>/purchase/', views.purchase_course, name='purchase_course'),
]
