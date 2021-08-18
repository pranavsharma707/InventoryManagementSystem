from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Order
from django.contrib.auth.decorators import login_required
from dashboardapp.forms import ProductForm,OrderForm,FileUploadForm
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

    order=Order.objects.filter(staff=request.user)
    orders=[]
    for data in order:
        dict={}
        dict['product']=data.product.name
        dict['category']=data.product.category
        dict['order_quantity']=data.order_quantity
        dict['price']=data.product.price
        dict['total']=data.order_quantity*data.product.price
        dict['date']=data.date
        orders.append(dict)

    sum=0
    for data in products:
        sum=sum+data.total_price

    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            product_id=request.POST['product']
            order_quantity=request.POST['order_quantity']
            product_quantity=Product.objects.get(id=product_id)
            if product_quantity.quantity==0:
                messages.success(request,f'{product_quantity.name} Product out of stock')
                return redirect('dashboard-index')
            elif product_quantity.quantity < int(order_quantity) or int(order_quantity)==0:
                                print(order_quantity,'order quantity')
                                messages.success(request,f'Please enter the quantity of {product_quantity.name} in range of stock')
                                return redirect('dashboard-index')
            else:
              product_quantity.quantity=product_quantity.quantity-int(order_quantity)
              product_quantity.save()
              instance.save()
              return redirect('dashboard-index')
           
            
    else:
        form=OrderForm()
    context={
        'total_price_products':sum,
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
    product_data=Product.objects.all()
    sum=0
    for data in product_data:
        sum=sum+data.total_price
    
    context={
        'total_price_products':sum,
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
    # items=Product.objects.raw('SELECT * FROM dashboardapp_product')
    items=Product.objects.all()
    sum=0
    for data in items:
        sum=sum+data.total_price
    # product_data=[]
    # for data in items:
    #     dict={}
    #     dict['id']=data.id
    #     dict['name']=data.name
    #     dict['category']=data.category
    #     dict['quantity']=data.quantity
    #     dict['price']=data.price
    #     dict['total']=data.quantity*data.price
    #     product_data.append(dict)
    workers_count=User.objects.all().count()
    products_count=Product.objects.all().count()
    orders_count=Order.objects.all().count()
    if request.method=='POST':
        data=request.FILES['file_upload']
        file=str(data)
        file_type=file[-3:]
        form=FileUploadForm(request.POST,request.FILES)
        if form.is_valid() and file_type=='csv':
                form.save()
                filepath=f'{settings.MEDIA_ROOT}documents/{data}'
                with open (filepath,'r') as csvfile:
                    csvreader=csv.DictReader(csvfile)
                    for row in csvreader:
                        if Product.objects.filter(name=row['name']).first():
                            pass
                        else:
                         product=Product(name=row['name'],category=row['category'],quantity=row['quantity'],price=row['price'])
                         product.save()
                os.remove(filepath)
                return redirect('dashboard-product')
        else:
            messages.success(request,'Only csv files is allowed')
            # product_name=form.cleaned_data.get('name')
            # messages.success(request,f"{product_name} has added")
            return redirect('dashboard-product')
    else:
        form=FileUploadForm()

    context={
        'total_price_products':sum,
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
    product_data=Product.objects.all()
    sum=0
    for data in product_data:
        sum=sum+data.total_price
    
    context={
        'total_price_products':sum,
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