from django.urls import path
from .views import *

urlpatterns = [
    #Auth
    path('signup/', signupuser),
    path('logout/', logoutuser, name="logoutuser"),
    #Todos
    path('', home, name="home"),
    path('current/', currenttodos, name="currenttodos"),


]