from django.urls import path
from .  import views


app_name='accountapp'

urlpatterns = [
    
        path('accountopen',views.accountopen,name='accountopen'),
        path('blank',views.blankfun,name='blankfun'),
        
]