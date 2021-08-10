from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
# @login_required(login_url='user-login') # means without authentication if you go any page then this login page is how

# Create your views here.
@login_required # this is any way after this in settings.py we have to set LOGIN_URL='user-login'
def home(request):
    return render(request,'dashboardapp/index.html')


# @login_required(login_url='user-login')
@login_required
def staff(request):
    return render(request,'dashboardapp/staff.html')

# @login_required(login_url='user-login')
@login_required
def product(request):
    return render(request,'dashboardapp/product.html')

# @login_required(login_url='user-login')
@login_required
def order(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'dashboardapp/order.html',context)