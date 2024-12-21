from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Permission
from django.urls import reverse

from .models import Product, Cart, Order, Bank_account

# Create your views here.
        
def product_detail(request, slug):
    user= request.user
    bank = get_object_or_404(Bank_account, user=user)
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'detail.html', {"product":product, "bank":bank})
    
def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"product": products})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)
    bank_account = get_object_or_404(Bank_account, user=user)
    print(product.stock)
    
    if bank_account.money - order.product.price > 0:
        if product.stock > 0:
            if created:
                cart.orders.add(order)
                cart.save()
                bank_account.money -= cart.orders.product.price
                bank_account.save()
                product.stock -= 1
                product.save()
                
            else:
                order.quantity += 1
                order.save()
                bank_account.money -= order.product.price
                bank_account.save()
                product.stock -= 1
                product.save()
    
    print(bank_account.money)
    return redirect(reverse("products", kwargs={"slug": slug}))

def cart(request):
    cart2 = get_object_or_404(Cart, user=request.user)
    products = Product.objects.all()
    return render(request, "cart.html", {"orders":cart2.orders.all(), "products": products})

def add_get_bank_account(request):
    user = request.user
    account, created = Bank_account.objects.get_or_create(user=user)
    bank_account = get_object_or_404(Bank_account, user=user)
    
    if created:
        bank_account.money = 1000
        bank_account.save()
    
    return render(request, "bank.html", {"bank": bank_account})

# -------------------------------------------------------------------------------------------

@permission_required("shop.is_worker", raise_exception=True)
def create_products(request):
    if request.method == "POST":
        form = produce.Boss(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect("frontpage")
    else:
        form = produce.Boss()
    return render(request, "new_products.html", {"form": form})