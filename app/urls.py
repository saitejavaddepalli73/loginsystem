from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index,name='home'),
   path('login/',views.Login,name='login'),
   path('index/',views.saveUser,name='saveuser'),
   path('userlogin/',views.userlogin,name='userlogin'),
   path('logout/',views.userlogout,name='logout'),
]
