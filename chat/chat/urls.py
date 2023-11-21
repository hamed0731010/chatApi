"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from chatAPI.views import ChatView , MessagesListApiView

get_members = ChatView.as_view({
    'get': 'get_members',
   
})
all=ChatView.as_view({'list':'all'})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/chat/user/<int:user_id>/members/', get_members),
    path('api/chat/messages/', MessagesListApiView.as_view()),
]
