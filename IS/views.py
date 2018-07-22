from django.shortcuts import render, redirect
from .forms import *


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
    form = GougingForm
    if request.method == 'POST':
        form = GougingForm(request.POST)

        if form.is_valid():
            gouging = form.save(commit=True)
            print('Созданная строжка:', gouging, gouging.start_date)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_gouging.html', {'form': form})


# Добавление наплавки
def add_surfacing(request):
    form = SurfacingForm

    if request.method == 'POST':
        form = SurfacingForm(request.POST)

        if form.is_valid():
            surfacing = form.save(commit=True)
            print('Созданная наплавка:', surfacing, surfacing.start_date)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_surfacing.html', {'form': form})


# Добавление термообработки
def add_heat_treatment(request):
    form = HeatTreatmentForm

    if request.method == 'POST':
        form = HeatTreatmentForm(request.POST)

        if form.is_valid():
            heat_treatment = form.save(commit=True)
            print('Созданная термообработка:', heat_treatment, heat_treatment.start_date)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_heat_treatment.html', {'form': form})


# Добавление механообработки
def add_machining(request):
    form = MachiningForm

    if request.method == 'POST':
        form = MachiningForm(request.POST)

        if form.is_valid():
            machining = form.save(commit=True)
            print('Созданная механообработка:', machining, machining.start_date)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_machining.html', {'form': form})


# Добавление главной таблицы
def add_primary_table(request):
    # Инициализируем все наши вложенные формы с различными префиксами
    form = PrimaryTableForm(prefix="prim")
    gouging_sub_form = GougingForm(prefix='gg')
    surfacing_sub_form = SurfacingForm(prefix='sg')
    heat_treatment_sub_form = HeatTreatmentForm(prefix='ht')
    machining_sub_form = MachiningForm(prefix='mg')

    # Проверяем метод
    if request.POST:
        # Загружаем наши формы снова, указываем в аргументе какой метод используем
        form = PrimaryTableForm(request.POST, prefix="prim")
        gouging_sub_form = GougingForm(request.POST, prefix='gg')
        surfacing_sub_form = SurfacingForm(request.POST, prefix='sg')
        heat_treatment_sub_form = HeatTreatmentForm(request.POST, prefix='ht')
        machining_sub_form = MachiningForm(request.POST, prefix='mg')

        # Убеждаемся в валидности всех форм
        if form.is_valid() and gouging_sub_form.is_valid() and surfacing_sub_form.is_valid() \
                and heat_treatment_sub_form.is_valid() and machining_sub_form.is_valid():

            # Подготавливаем модель главной таблицы, но не коммитим её в бд.
            pt = form.save(commit=False)

            # Сохраняем все поля с ForeignKey (наши подформы)
            pt.gouging = gouging_sub_form.save()
            pt.surfacing = surfacing_sub_form.save()
            pt.heat_treatment = heat_treatment_sub_form.save()
            pt.machining = machining_sub_form.save()

            # Сохраняем главную таблицу
            pt.save()
            return redirect('/')
        else:
            print(form.errors, gouging_sub_form.errors, surfacing_sub_form.errors,
                  heat_treatment_sub_form.errors, machining_sub_form.errors)

    return render(request, 'add_primary_table.html',
                  {
                      'form': form, 'gouging_sub_form': gouging_sub_form,
                      'surfacing_sub_form': surfacing_sub_form,
                      'heat_treatment_sub_form': heat_treatment_sub_form,
                      'machining_sub_form': machining_sub_form
                  })
