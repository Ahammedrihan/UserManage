from django.urls import path
from .import views

urlpatterns = [
    path('',views.hello),
    path('login/',views.user_login),
    path('signup/',views.user_signup)
]



