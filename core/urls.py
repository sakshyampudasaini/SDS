from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import home
from django import views 

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', home, name='home'),  # Homepage
        path('', views.home, name='home'),  # Add a root route

    path('students/', include('students.urls')),
]
