from django.urls import path
from .import views
urlpatterns = [
    path('',views.Home),
    path('Home',views.index),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="Logout"),
    path('Signup',views.signup,name="Signup"),
    path("Contact",views.Contact, name = "Contact"),
]
