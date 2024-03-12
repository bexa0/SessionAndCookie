from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render


def start_view(request):
    # Отправка уведомлений через сессию
    request.notifications = [
        (messages.SUCCESS, "Успешное уведомление"),
        (messages.ERROR, "Ошибка"),
    ]

    return render(request, 'app/start.html')
