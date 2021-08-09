from django.urls import path
from dashboardapp.views import *

urlpatterns = [
path('',home,name='dashboard-index'),
path('staff/',staff,name='dashboard-staff'),
path('product/',product,name='dashboard-product'),
path('order/',order,name='dashboard-order'),
]


