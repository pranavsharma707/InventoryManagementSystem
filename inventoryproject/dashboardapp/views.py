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
    items=Product.objects.raw('SELECT * FROM dashboardapp_product')
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm()

    context={
        'items':items,
        'form':form
    }
    return render(request,'dashboardapp/product.html',context)

# @login_required(login_url='user-login')
@login_required
def order(request):
    product=Product.objects.all()
    context={
        'product':product
    }
    return render(request,'dashboardapp/order.html',context)


def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboardapp/product_delete.html')

def product_update(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)# here fill the data and it is updated
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm(instance=item)# here without based on id data by dafault comes in field based on id means instance=item
    context={
        'form':form
    }
    return render(request,'dashboardapp/product_update.html',context)