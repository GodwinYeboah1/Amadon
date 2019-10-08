from django.shortcuts import render,redirect

# Create your views here.

def index(r):
    return render(r, "index.html")

def create_purchase(r):
    product_id = r.POST['product_id']
    quantity = r.POST['quantity']

    if product_id == "1015":
        price = 19.99
    elif product_id == "1016":
        price = 29.99
    elif product_id == "1017":
        price = 4.99
    elif product_id == "1018":
        price = 49.99
    else:
        price = 0

    r.session['total_amount'] = int(quantity) * price
    r.session['quantity'] = quantity
    r.session['product_price'] = price

    return redirect('/amadon/checkout')

def display_purchase(r):

    context = {
        'total_amount':  r.session['total_amount'],
        'total_quantity':  r.session['quantity'],
        'product_price':  r.session['product_price'],
    }
    return render(r,'checkout_page.html', context)