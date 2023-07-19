from django.shortcuts import render
from Menu.models import *
from .forms import *


def change(request, dish_id):
    dishes = Dish.objects.get(id=dish_id)

    initial_data = {
        'image': dishes.image,
        'name': dishes.name,
        'category': dishes.category,
        'weight': dishes.weight,
        'price': dishes.price,
        'discount': dishes.discount,
        'alergic': dishes.alergic,
        'description': dishes.description
    }
    form = ChangeForm(initial=initial_data)

    if request.method == 'POST':
        form = ChangeForm(request.POST, request.FILES, instance=dishes)
        if form.is_valid():
            form.save()
            # """            if 'image' in request.FILES:
            #     dishes.image = request.FILES['image']
            # Dish.objects.filter(id=dish_id).update(name='name', image='image', category='category', weight='weight', price='price', discount='discount', alergic='alergic', description='description')()
            # # Другие действия после сохранения формы...


    else:

        initial_data = {
            'image': dishes.image,
            'name': dishes.name,
            'category': dishes.category,
            'weight': dishes.weight,
            'price': dishes.price,
            'discount': dishes.discount,
            'alergic': dishes.alergic,
            'description': dishes.description
        }

        form = ChangeForm(instance=dishes, initial=initial_data)

    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'Manager_page/Change.html', {'form': form, 'dishes': dishes})



