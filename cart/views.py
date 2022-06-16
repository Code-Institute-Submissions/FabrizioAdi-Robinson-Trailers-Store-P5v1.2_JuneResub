from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

# Add to cart

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

# Add item to the cart

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

# Update quantity

def update_cart(request, item_id):
    """ Update the quantity of the specified product to specifing amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        del cart[item_id]
        if not cart[item_id]:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# Remove from Cart

def remove_from_cart(request, item_id):
    """ Remove item from shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})
    cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return HttpResponse(status=200)
