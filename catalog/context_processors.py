# coding=utf-8

from .models import Category
#from catalog.models import Category

def categories(request):
    return {
        'categories': Category.objects.all()
    }
