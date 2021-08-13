"""inventoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('dashboardapp.urls')),
    path('register/',user_view.register,name='user-register'),
    path('',auth_views.LoginView.as_view(template_name='user/login.html'),name="user-login"),
    # here we get LoginView Class from view package and make our own template means login.html and 
    #in this {{form}} means form django-admin
    path('profile/',user_view.profile,name='user-profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name="user-logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    #here password_reset is my own customize template
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name="password_reset_complete")
    #here PasswordResetView is an built in class django-admin
    #if you use password resset of django admin then PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView compulsory required
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

