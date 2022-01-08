from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

import products
from .models import Product
from django.views import generic
from django.utils import timezone
# Create your views here.
def index(request):
    product=Product.objects.all()
    return render(request, 'index.html',{'product': product})

def detail(request, product_id):
    product=get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

def cart(request, product_id):
        product=get_object_or_404(Product, pk=product_id)
        return render(request, 'products/cart.html', {'product': product})

def checkout(request, product_id):
        product=get_object_or_404(Product, pk=product_id)
        return render(request, 'products/checkout.html', {'product': product})
    
def confirmation(request, product_id):
        product=get_object_or_404(Product, pk=product_id)
        return render(request, 'products/confirmation.html', {'product': product})
    

# class DetailView(generic.ListView):
#     model = Product
#     template_name = 'products/detail.html',
    
#     {
#         'product': products
#     }

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Product.objects.filter(pub_date__lte=timezone.now())

    
    
# def detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, 'products/detail.html', {'product': product})



# def cart(request):
#     product = Product.objects.all()
#     return render(request, 'cart.html',{'product': product})

# def checkout(request, product_id):
#     return render(request, '/checkout.html')

# def confirmation(request):
#     product = Product.objects.all()
#     return render(request, 'confirmation.html',{'product': product})

# def productsingle(request, my_id):
#     return render(request, 'product-single.html')