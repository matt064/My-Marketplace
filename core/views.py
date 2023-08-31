from django.shortcuts import render, redirect
from django.contrib.auth import logout

from item.models import Category, Item
from .forms import SingupForm, LoginForm




def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'core/index.html', context)


def contact(request):
    
    context = {}
    return render(request, 'core/contact.html', context)


def singup(request):
    form = SingupForm()
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')

    context = {'form': form}
    return render(request, 'core/singup.html', context)


def logoutPage(request):
    logout(request)
    return redirect('core:index')
    