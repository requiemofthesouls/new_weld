from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render, render_to_response
from django.utils.decorators import method_decorator
from django.views.generic import (ListView, UpdateView)

from .forms import (
    PrimaryTableForm,
    GougingForm,
    SurfacingForm,
    AdditionalSurfacingForm,
    HeatTreatmentForm,
    MachiningForm,
    FinalSurfacingForm,
    MaterialForm
)
from .models import (
    PrimaryTable,
    Surfacing,
    HeatTreatment)


def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)


class Main(ListView):
    template_name = 'main.html'
    context_object_name = 'tables'
    queryset = PrimaryTable.objects.order_by('-received_stamp_date')


# def main(request):
#     context_dict = {'tables': PrimaryTable.objects.order_by('-received_stamp_date')}
#     return render(request, 'main.html', context_dict)


# class Main(UpdateView):
#     model = PrimaryTable
#     template_name = 'primary_tables_edit.html'
#     form_class = PrimaryTableForm
#     queryset = PrimaryTable.objects.order_by('-received_stamp_date')
#
#     def get_object(self, queryset=queryset):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(PrimaryTable, id=id_)
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)


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
            print(
                'Созданная термообработка:',
                heat_treatment,
                heat_treatment.start_date)
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
            print(
                'Созданная механообработка:',
                machining,
                machining.start_date)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'add_machining.html', {'form': form})


# Добавление главной таблицы
def add_primary_table(request):
    # Инициализируем все наши вложенные формы с различными префиксами
    form = PrimaryTableForm(prefix="primary_table_form")
    gouging_sub_form = GougingForm(prefix='gouging_sub_form')
    surfacing_sub_form = SurfacingForm(prefix='surfacing_sub_form')
    additional_surfacing_sub_form = AdditionalSurfacingForm(
        prefix='additional_surfacing_sub_form')
    final_surfacing_sub_form = FinalSurfacingForm(
        prefix='final_surfacing_sub_form')
    heat_treatment_sub_form = HeatTreatmentForm(
        prefix='heat_treatment_sub_form')
    machining_sub_form = MachiningForm(prefix='machining_sub_form')

    # Проверяем метод
    if request.POST:
        # Загружаем наши формы снова, указываем в аргументе какой метод
        # используем
        form = PrimaryTableForm(request.POST, prefix="primary_table_form")
        gouging_sub_form = GougingForm(request.POST, prefix='gouging_sub_form')
        surfacing_sub_form = SurfacingForm(
            request.POST, prefix='surfacing_sub_form')
        additional_surfacing_sub_form = AdditionalSurfacingForm(
            request.POST, prefix='additional_surfacing_sub_form')
        final_surfacing_sub_form = FinalSurfacingForm(
            request.POST, prefix='final_surfacing_sub_form')
        heat_treatment_sub_form = HeatTreatmentForm(
            request.POST, prefix='heat_treatment_sub_form')
        machining_sub_form = MachiningForm(
            request.POST, prefix='machining_sub_form')

        # Убеждаемся в валидности всех форм
        if form.is_valid() \
                and gouging_sub_form.is_valid() \
                and heat_treatment_sub_form.is_valid() \
                and machining_sub_form.is_valid() \
                and surfacing_sub_form.is_valid() \
                and additional_surfacing_sub_form.is_valid() \
                and final_surfacing_sub_form.is_valid():

            # Подготавливаем модель главной таблицы, но не коммитим её в бд.
            pt = form.save(commit=False)

            # Сохраняем все поля с ForeignKey (наши подформы)
            pt.gouging = gouging_sub_form.save()

            # Для наплавки, т.к. там есть своя подформа (дополнительная наплавка)
            # делаем так:
            # 1. Сохраняем Наплавку
            # 2. Указываем Нашу дополнительную наплавку
            # 3. Сохраняем наплавку ещё раз
            pt.surfacing = surfacing_sub_form.save()

            if additional_surfacing_sub_form.cleaned_data['amount_of_material']:
                pt.surfacing.additional_surfacing = additional_surfacing_sub_form.save()
                if final_surfacing_sub_form.cleaned_data['amount_of_material']:
                    pt.surfacing.final_surfacing = additional_surfacing_sub_form.save()
            pt.surfacing.save()

            pt.heat_treatment = heat_treatment_sub_form.save()
            pt.machining = machining_sub_form.save()

            # Сохраняем главную таблицу
            pt.save()
            return redirect('/')
        else:
            print(
                form.errors,
                gouging_sub_form.errors,
                surfacing_sub_form.errors,
                heat_treatment_sub_form.errors,
                machining_sub_form.errors,
                additional_surfacing_sub_form.errors,
                final_surfacing_sub_form.errors)

    return render(request,
                  'add_primary_table.html',
                  {'form': form,
                   'gouging_sub_form': gouging_sub_form,
                   'heat_treatment_sub_form': heat_treatment_sub_form,
                   'machining_sub_form': machining_sub_form,
                   'surfacing_sub_form': surfacing_sub_form,
                   'additional_surfacing_sub_form': additional_surfacing_sub_form,
                   'final_surfacing_sub_form': final_surfacing_sub_form,
                   })


def test_profile_settings(request):
    """
    Allows a user to update their own profile.
    """
    # user = request.user

    # Create the formset, specifying the form and formset we want to use.
    # LinkForm == MaterialForm
    MaterialFormSet = formset_factory(MaterialForm)

    # Get our existing link data for this user.  This is used as initial data.
    # user_links = UserLink.objects.filter(user=user).order_by('anchor')
    # link_data = [{'anchor': l.anchor, 'url': l.url}
    #                 for l in user_links]

    if request.method == 'POST':
        # profile_form == surfacing_form
        # link_formset == material_formset
        surfacing_form = SurfacingForm(request.POST)
        material_formset = MaterialFormSet(request.POST)

        if surfacing_form.is_valid() and material_formset.is_valid():
            # Save user info
            # user.first_name = profile_form.cleaned_data.get('first_name')
            # user.last_name = profile_form.cleaned_data.get('last_name')
            # user.save()

            # Now save the data for each form in the formset
            new_materials = []

            for material_form in material_formset:
                type_of_consumables = material_form.cleaned_data.get(
                    'type_of_consumables')
                amount_of_material = material_form.cleaned_data.get(
                    'amount_of_material')

                if type_of_consumables and amount_of_material:
                    new_materials.append(
                        Surfacing(
                            type_of_consumables=type_of_consumables,
                            amount_of_material=amount_of_material))

            try:
                with transaction.atomic():
                    # Replace the old with the new
                    Surfacing.objects.filter(
                        type_of_consumables=type_of_consumables,
                        amount_of_material=amount_of_material).delete()
                    Surfacing.objects.bulk_create(new_materials)

                    # And notify our users that it worked
                    messages.success(request, 'You have updated your profile.')

            except IntegrityError:  # If the transaction failed
                messages.error(
                    request, 'There was an error saving your profile.')
                return redirect(reverse('profile-settings'))

    else:
        profile_form = ProfileForm(user=user)
        link_formset = LinkFormSet(initial=link_data)

    context = {
        'profile_form': profile_form,
        'link_formset': link_formset,
    }

    return render(request, 'our_template.html', context)


class HeatTreatmentList(ListView):
    model = HeatTreatment
    queryset = HeatTreatment.objects.order_by('-start_date')
    template_name = 'heat_treatment_list.html'
    paginate_by = 10
    context_object_name = 'heat_treatment'


class HeatTreatmentDetail(PermissionRequiredMixin, UpdateView):
    model = HeatTreatment
    context_object_name = 'heat_treatment'
    template_name = 'heat_treatment_detail.html'
    fields = ['id', 'final_hardness', 'start_date']
    template_name_suffix = '_update_form'
    permission_required = ('IS.change_heattreatment',
                           'IS.view_heattreatment',
                           'IS.add_heattreatment')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('app/add')


def page_not_found(request, exception, template_name='404.html'):
    response = render_to_response("404.html")
    response.status_code = 404
    return response
