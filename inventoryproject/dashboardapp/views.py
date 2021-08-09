from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'dashboardapp/index.html')

def staff(request):
    return render(request,'dashboardapp/staff.html')

def product(request):
    return render(request,'dashboardapp/product.html')



def order(request):
    return render(request,'dashboardapp/order.html')
