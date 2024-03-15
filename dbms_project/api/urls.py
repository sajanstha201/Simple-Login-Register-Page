from django.urls import path,include
from main.views import file,login_function,post,tweets,register_api,login_api
urlpatterns=[
    path('data/',file,name='data_url'),
    path('login/',login_function,name='login_function_url'),
    path('post/',post,name='post_url'),
    path('tweets/',tweets.as_view(),name='tweets_url'),
    path('register_api/',register_api.as_view(),name='register_api_url'),
    path('login_api/',login_api.as_view(),name="login_api_url")
]