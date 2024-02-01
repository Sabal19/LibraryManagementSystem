from django.urls import path
from . import views, apiview

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('detail',apiview.Detail,name='detail'),
    path('detail/<str:pk>',apiview.DetailbyID,name='detailbyID'),

]