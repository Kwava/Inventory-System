from django.shortcuts import redirect, render
from .models import Order, Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateProductForm, OrderForm
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    orders=Order.objects.all()
    order_count=orders.count()
    products=Product.objects.all()
   # if request.method=="POST":
      #  form=OrderForm(request.POST)
    #else:
     #   form=OrderForm()
    context={'orders':orders,
             'order_count':order_count,
             'products':products,
             }
    return render(request,'Dashbord/index.html',context)

@login_required
def product(request):
    product=Product.objects.all()
   
    if request.method=="POST":
        Form=CreateProductForm(request.POST)
        if Form.is_valid():
            name=Form.cleaned_data['name']
            category=Form.cleaned_data['category']
            quantity=Form.cleaned_data['quantity']
            register=Product(name=name,category=category,quantity=quantity)
            register.save()
            product_name=Form.cleaned_data.get('name')
            messages.success(request,f'{product_name} ajoute avec succe')
            Form=CreateProductForm()   
    else:
        Form= CreateProductForm()
    products=Product.objects.all()
    context={
             'product':products, 
             'Form':Form,
             }
    
    return render(request,'Dashbord/product.html',context
     )
@login_required
def delete_product(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=='POST':
        product.delete()
        return redirect('Dashbord-product')
    return render(request,'Dashbord/product_delete.html',context={'product':product,})
   
@login_required
def update_product(request,pk):
    product=Product.objects.get(id=pk)
    if request.method=="POST":
        Form=CreateProductForm(request.POST, instance=product)
        if Form.is_valid():
            product.save()
            return redirect('Dashbord-product') 
    else:
        Form= CreateProductForm(instance=product)
    context={
        'product':product,
        'Form':Form,
    }
    return render(request,'Dashbord/product_update.html',context)
    


@login_required
def order(request):
    orders=Order.objects.all()
    orders_count=orders.count()
    workers_count=User.objects.all().count()
    product_count=Product.objects.all().count()
    context={
        'orders':orders,
        'product_count':product_count,
        'workers_count':workers_count,
        'orders_count':orders_count,
             
             }
    return render(request,'Dashbord/order.html',context)

@login_required
def staff(request):
    workers=User.objects.all()
    product_count=Product.objects.all().count()
    orders_count=Order.objects.all().count()
    workers_count=workers.count()
    
    context={
        'workers':workers,
        'workers_count':workers_count,
        'orders_count': orders_count,
        'product_count':product_count
        
    }
    return render(request,'Dashbord/staff.html',context)

@login_required
def staff_detail(request, pk):
    workers=User.objects.get(id=pk)
    context={'workers':workers}
    return render(request,'Dashbord/staff_detail.html',context)



