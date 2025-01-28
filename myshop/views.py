from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.


def home(request):
    return render(request, 'home.html')
    
def list(request):
   
    category = request.GET.get('category', None)

    categories = Category.objects.all()

    if category:
        products = Product.objects.filter(category=category, available=True)
    else:
        products = Product.objects.all()

    
    return render(request, 'list.html', {'products': products, 'categories': categories, 'category': category})

def detalles(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detalles.html', {'product':product})