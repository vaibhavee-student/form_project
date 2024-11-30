from django.urls import path
from . import views 

urlpatterns = [
    path("",views.main,name='main'),
    path("calculate/",views.calculator,name='calculator'),
]