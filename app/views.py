from django.shortcuts import render, redirect
import requests
from .forms import BookForm
from .models import Book

TELEGRAM_BOT_TOKEN = '7737269082:AAFfna3Dz36gYRkNwZeRq7JFu17cH4GSVaE' 
TELEGRAM_CHAT_ID = '5120556374' 

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    # Добавляем базовую обработку ошибок для внешних запросов
    try:
        requests.post(url, data=data)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке сообщения в Telegram: {e}")

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save() # Сохраняем экземпляр книги
            # Создаем сообщение для Telegram, используя данные сохраненной книги
            message = f"<b>Добавлена новая книга:</b>\n" \
                      f"<b>Название:</b> {book.title}\n" \
                      f"<b>Автор:</b> {book.author}"
            # Предполагается, что ваша модель Book имеет поля 'title' и 'author'.
            # Скорректируйте содержимое сообщения в соответствии с полями вашей модели Book.

            send_telegram_message(message) # Вызываем функцию отправки сообщения
            return redirect('add_book')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})






# from django.shortcuts import render, redirect
# from .forms import BookForm
# from .models import Book

# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_book')
#     else:
#         form = BookForm()
#     return render(request, 'add_book.html', {'form': form})