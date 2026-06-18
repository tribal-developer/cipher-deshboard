from django.urls import path, include
from .views import *

urlpatterns = [    
    path('admin/', admin_dashboard, name='admin_dashboard'),
    path('user/', user_dashboard, name='user_dashboard'),
    path('add-record/', add_record, name='add_record'),
    path('authorised-users/', authorised_users,name='authorised_users'),
    path('authorise-user/', authorise_user,name='authorise_user'),
    path('edit/<int:pk>/', edit_record, name='edit_record'),
    path('delete/<int:pk>/', delete_record, name='delete_record'),   
    path('help/', help_page, name='help_page'),
    path('auth-users/', auth_users, name='auth_users'),   
]