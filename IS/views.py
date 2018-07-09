from django.shortcuts import render, redirect
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
    return render(request, 'add_gouging.html', {'form': form})


# Добавление наплавки
def add_surfacing(request):
    form = SurfacingForm()

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
    form = HeatTreatmentForm()

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
    form = MachiningForm()

    if request.method == 'POST':
        form = MachiningForm(request.POST)

        if form.is_valid():
            machining = form.save(commit=True)
            print('Созданная термообработка:', machining, machining.start_date)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_machining.html', {'form': form})


# Добавление главной таблицы
def add_primary_table(request):
    form = PrimaryTableForm

    if request.method == 'POST':
        form = PrimaryTableForm(request.POST)

        if form.is_valid():
            primary_table = form.save(commit=True)
            print('Созданная термообработка:', primary_table)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_primary_table.html', {'form': form})


FORMS = [
    ("gouging", GougingForm),
    ("surfacing", SurfacingForm),
    ("heat_treatment", HeatTreatmentForm),
    ("machining", MachiningForm)
]

TEMPLATES = {
    "gouging": "add_gouging.html",
    "surfacing": "add_surfacing.html",
    "heat_treatment": "add_heat_treatment.html",
    "machining": "add_machining.html",
}


# class AddPrimaryTableWizard(SessionWizardView):
#     def get_template_names(self):
#         return [TEMPLATES[self.steps.current]]
#
#     def get_context_data(self, form, **kwargs):
#         context = super(AddStudentWizard, self).get_context_data(form=form, **kwargs)
#         if self.steps.current == 'contract':
#             context.update({'ok': 'True'})
#         return context
#
#     def done(self, form_list, **kwargs):
#         student_form = form_list[0].cleaned_data
#         contract_form = form_list[1].cleaned_data
#         s = Student.objects.create(
#             sex=student_form['sex'],
#             citizenship=student_form['citizenship'],
#             doc=student_form['doc'],
#             student_document_type=student_form['student_document_type'],
#             parent_document_type=student_form['parent_document_type']
#         )
#         f = FioChange.objects.create(
#             student=s,
#             event_date=student_form['event_date'],
#             fio=student_form['fio']
#         )
#         c = Contract.objects.create(
#             student=s,
#             number=contract_form['number'],
#             student_home_phone=contract_form['phone']
#         )
#         return HttpResponseRedirect(reverse('liststudent'))
