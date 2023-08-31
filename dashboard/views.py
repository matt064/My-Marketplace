from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from item.models import Item, Category



@login_required
def index(request):
    """pomyslec nad dokladnym okresneniem przedmiotow z danej kategorii uzytkownika"""
    category_id = request.GET.get('category_id', 0)
    items = Item.objects.filter(created_by=request.user)
    categories = Category.objects.filter(items__created_by=request.user)

    if category_id:
        items = items.filter(category_id=category_id)


    context = {'items':items, 'categories':categories}
    return render(request, 'dashboard/index.html', context)


