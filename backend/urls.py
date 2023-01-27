from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='Home'),
    path('addnotices/',views.add_notice, name='addnotices'),
    path('login/',views.user_login, name='login')
]
