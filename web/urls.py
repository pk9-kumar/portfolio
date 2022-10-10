from django.urls import path
from .views import index, comming_soon

urlpatterns = [
    path('', index, name='index'),
    path('comming_soon/', comming_soon, name='comming_soon'),

]
