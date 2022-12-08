from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('user_login',views.user_login,name = "user_login"),
    path('user_register',views.user_register,name = "user_register"),
    path('user/user_login',views.user_login,name = "user_login"),
    path('user_logout',views.user_logout,name = "user_logout")

]