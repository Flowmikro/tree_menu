from django.shortcuts import render
from django.shortcuts import get_object_or_404

from app.models import MenuModel


def menu_list(request, menu_name):
    menu = get_object_or_404(MenuModel, named_url=menu_name)
    context = {'menu': menu}
    return render(request, 'app/menu.html', context)