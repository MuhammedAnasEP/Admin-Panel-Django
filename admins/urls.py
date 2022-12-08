from django.urls import path
from . import views
urlpatterns = [
    path('',views.admins_home,name='admin'),
    path('admins_log',views.admins_log,name = 'admins_log'),
    path('admins_login',views.admins_login,name = 'admins_login'),
    path('admins_home',views.admins_home,name = 'admins_home'),
    path('admins_logout',views.admins_logout,name='admins_logout'),
    path('admins_inse',views.admins_inse,name='admins_inse'),
    path('admins_insert',views.admins_insert,name='admins_insert'),
    path('admins_edit/<int:id>',views.admins_edit,name='admins_edit'),
    path('admins_update/<int:id>',views.admins_update,name='admins_update'),
    path('admins_delete/<int:id>',views.admins_delete,name='admins_delete')
]