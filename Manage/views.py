from django.shortcuts import render, get_object_or_404, redirect
from Contact.models import *
from .forms import *
from Menu.models import *

def manage(request):
    categories = DishCategory.objects.filter()
    orders = Order.objects.filter()
    dishs = Dish.objects.filter()

    session_key = request.session.session_key
    form = ManageForm(request.POST or None)
    if request.method == 'POST':
        form = ManageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    family = 1
    return render(request, 'Manager_page/Manage.html', locals())

def delete_orders(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('/manage')

def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.delete()
    return redirect('/manage')

def confirm_orders(request, order_id):
    Order.objects.filter(id=order_id).updated(status=True)
    return redirect('/manage')
