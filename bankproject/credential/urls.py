from django.urls import path
from .  import views


app_name='credential'

urlpatterns = [
        path('registration',views.regfun,name='regfun'),
        path('login',views.logfun,name='logfun'),
        path('logout',views.logoutfun,name='logoutfun'),
]