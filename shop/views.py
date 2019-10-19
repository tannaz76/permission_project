from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)





def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    permission_classes = [AllowAny,]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }

    
    return render(request, 'shop/product/list.html', context)


@login_required
@permission_required ('can_see_product_detail')
@permission_required ('can_add_new_product')
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    permission_classes = [IsAuthenticated,]
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, 'shop/product/detail.html', context)

