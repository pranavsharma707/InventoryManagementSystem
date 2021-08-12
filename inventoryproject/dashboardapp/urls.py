from django.urls import path
from dashboardapp.views import *

urlpatterns = [
path('',home,name='dashboard-index'),
path('staff/',staff,name='dashboard-staff'),
path('product/',product,name='dashboard-product'),
path('staff/detail/<int:pk>',staff_detail,name='dashboard-staff-detail'),
path('product/',product,name='dashboard-product'),
path('product/delete/<int:pk>/',product_delete,name='dashboard-product-delete'),
path('product/update/<int:pk>/',product_update,name='dashboard-product-update'),
path('order/',order,name='dashboard-order'),
]


