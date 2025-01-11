from django.urls import path
from .views import *

urlpatterns = [

    path('', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('test/', test),
]
