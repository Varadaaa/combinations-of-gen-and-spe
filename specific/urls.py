from specific.views import *

from django.urls import path


app_name= 's'


urlpatterns =[
    path('spe/', spe, name='spe'),
    path('spe2/', spe2, name='spe2'),
]