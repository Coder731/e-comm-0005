from django.shortcuts import render
from .models import Item

def item_list(request):
    context = {
        'items': Items.objects.all()
    }
    return  render(request, "item_list.html", context)