from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.register,name='register_url'),
    path('login/',views.login,name='login_url'),
    path('logout/',views.logout,name='logout_url'),
]
