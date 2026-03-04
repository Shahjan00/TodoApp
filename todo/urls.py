from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('todo', views.todo, name='tasks'),
    path('edit_todo/<int:id>', views.edit_todo, name='edit_todo'),
    path('del_todo/<int:id>', views.del_todo, name="Del_todo" ),
]
