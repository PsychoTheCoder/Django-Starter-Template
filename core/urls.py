from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('login/', views.handleLogin, name="login"),
    path('signup/', views.handleSignup, name="signup"),
    path('logout/', views.handlelogout, name="logout"),

]
