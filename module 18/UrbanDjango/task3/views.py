from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'index.html', context)

def shop(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    return render(request, 'shop.html', context)

def cart(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)
