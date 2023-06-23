"""
URL configuration for todo_list project.

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
from django.urls import path, include # include is used to include other URLconfs
from home_page.views import home_route
from todo_app.views import todo_list, todo_create, todo_update, todo_delete


urlpatterns = [
    # The first argument is the path
    # The second argument is the function to call
    # The third argument is the name of the path. The name is used to refer to the path in the templates
    path('', home_route, name='home_page'),
    path('todos/', todo_list, name='todo_list'),
    path('todos/create/', todo_create, name='todo_create'),
    path('todos/update/<int:pk>/', todo_update, name='todo_update'),
    path('todos/delete/<int:pk>/', todo_delete, name='todo_delete'),
]
