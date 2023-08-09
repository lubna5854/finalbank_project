
from django.urls import path
from .  import views


app_name='bankapp'

urlpatterns = [
        path('',views.bankfun,name='bankfun'), 
        path('drop',views.dropfun,name='dropfun'),   
       ]