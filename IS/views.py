from django.shortcuts import render, redirect
from django.db.models import Q
import operator
from .models import PrimaryTable
from .forms import *
from django.utils import timezone


def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)


def main(request):
    context_dict = {'tables': PrimaryTable.objects.order_by('-received_stamp_date')}
    return render(request, 'main.html', context_dict)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        tables = PrimaryTable.objects.filter(number__icontains=q)
        return render(request, 'search.html', {'tables': tables, 'query': q})
    else:
        return redirect('/')


# Добавление строжки
def add_gouging(request):
    form = GougingForm()

    if request.method == 'POST':
        form = GougingForm(request.POST)

        if form.is_valid():
            gouging = form.save(commit=True)
            print('Созданная строжка:', gouging, gouging.start_date)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'test.html', {'form': form})
