from django.shortcuts import render
from django.http import JsonResponse
from Contact.models import Order

def save_data(request):
    session_key = request.session.session_key
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        seats = request.POST.get('seats')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Создание нового объекта Order и сохранение данных в БД
        order = Order(date=date, time=time, seats=seats, name=name, email=email, phone=phone)
        order.save()

        # Возвращение JSON-ответа, если требуется
        return JsonResponse({'success': True})

    return render(request, 'Reservation.html')
