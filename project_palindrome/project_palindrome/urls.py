"""
URL configuration for project_palindrome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from app_game.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createUser/', create_new_user),
    path('updateUser/', update_user),
    path('deleteUser/', delete_user),
    path('login/', login_user),
    path('logout/', logout_user),
    path('startGame/', start_game),
    path('getBoard/', get_board),
    path('updateBoard/', update_board),
    path('getGameList/', get_game_list),
]
