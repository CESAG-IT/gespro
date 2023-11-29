from django.shortcuts import render,get_object_or_404,redirect

from products.forms import CreateProductForm
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, "products/index.html", context)

def create(request):

    if request.method == 'GET':
        form = CreateProductForm()
        context = {
            'form': form,
        }
        return render(request, "products/create.html", context)
    else: 
        form = CreateProductForm(request.POST, request.FILES)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect("index")
        else: 
            return render(request, "products/create.html",context)


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = CreateProductForm(instance=product)
        context = {
            "product": product,
            'form': form,
        }
        return render(request, "products/update.html", context)
    else: 
        form = CreateProductForm(request.POST, request.FILES, instance=product)
       
        if form.is_valid():
            form.save()
            return redirect("index")
        else: 
            context = {
                "product": product,
                'form': form
            }
            return render(request, "products/update.html",context)
    

def delete(request, pk):

    product = get_object_or_404(Product, pk=pk)
    try:
        product.delete()
    except Exception as e:
        print(e)

    return redirect('index')  
