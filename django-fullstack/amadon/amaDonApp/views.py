from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def clear(request):
    request.session.clear()
    return(redirect('/'))

def order(request):
    price_form = Product.objects.get(id = request.POST['product_id']).price
    quantity_form = int(request.POST["quantity"])
    total_charge = quantity_form * price_form
    order = Order.objects.create(quantity_ordered=quantity_form, total_price=total_charge)
    return redirect(f'/checkout/{order.id}')

def checkout(request, order_id):
    order = Order.objects.get(id=order_id)
    all_orders = Order.objects.all()

    all_orders_price = 0
    all_orders_total_quantity = 0

    for order in all_orders:
        all_orders_price += order.total_price
        all_orders_total_quantity += 1

    context = {
        'quantity' :  order.quantity_ordered,
        'charged' :  order.total_price,
        'all_orders_price' : all_orders_price,
        'all_orders_total_quantity' : all_orders_total_quantity
    }
    return render(request, "checkout.html", context)
