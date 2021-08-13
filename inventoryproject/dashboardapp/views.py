from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Order
from django.contrib.auth.decorators import login_required
from dashboardapp.forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# @login_required(login_url='user-login') # means without authentication if you go any page then this login page is how

# Create your views here.
@login_required # this is any way after this in settings.py we have to set LOGIN_URL='user-login'
def home(request):
    orders=Order.objects.all()
    products=Product.objects.all()
    workers_count=User.objects.all().count()
    orders_count=Order.objects.all().count()
    products_count=Product.objects.all().count()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count
    }    
    return render(request,'dashboardapp/index.html',context)

# @login_required(login_url='user-login')
@login_required
def staff(request):
    workers=User.objects.all()
    workers_count=workers.count()
    products_count=Product.objects.all().count()
    orders_count=Order.objects.all().count()
    
    context={
        'workers':workers,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count
    }
    return render(request,'dashboardapp/staff.html',context)

@login_required
def staff_detail(request,pk):
    workers=User.objects.get(id=pk)
    workers_count=workers.count()
    products_count=Product.objects.all().count()
    orders_count=Order.objects.all().count()
    
    context={
        'workers':workers,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count
    }
    return render(request,'dashboardapp/staff_detail.html',context)

# @login_required(login_url='user-login')
@login_required
def product(request):
    items=Product.objects.raw('SELECT * FROM dashboardapp_product')
    workers=User.objects.all()
    workers_count=workers.count()
    products_count=Product.objects.all().count()
    orders_count=Order.objects.all().count()
    
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f"{product_name} has added")
            return redirect('dashboard-product')
    else:
        form=ProductForm()

    context={
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count
    }
    return render(request,'dashboardapp/product.html',context)

# @login_required(login_url='user-login')
@login_required
def order(request):
    orders=Order.objects.all()
    workers_count=workers.count()
    products_count=Product.objects.all().count()
    orders_count=Order.objects.all().count()
    
    context={
        'orders':orders,
        'workers_count':workers_count,
        'products_count':products_count,
        'orders_count':orders_count
    }
    return render(request,'dashboardapp/order.html',context)

@login_required
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboardapp/product_delete.html')

@login_required
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