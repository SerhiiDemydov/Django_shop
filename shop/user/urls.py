"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from user.views import UserDetailView, UserUpdateView

from .views import signup

app_name = "user"

urlpatterns = [
    path('<int:pk>/profile/', UserDetailView.as_view(), name="profile"),
    path('create/',  signup, name="create-user"),
    # path('create/success', UserDetailView.as_view(), name="create-user-success"),
    path('<int:pk>/update/', UserUpdateView.as_view(), name="update-user"),
]


