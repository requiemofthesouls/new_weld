def AAAAAAA(request):
    # Инициализируем все наши вложенные формы с различными префиксами
    form = PrimaryTableForm(prefix="primary_table_formfsdfffffffffffffffffffffffffffffffffffffffffffffffffffffffff")
    gouging_sub_form = GougingForm(prefix='gouging_sub_formdsfhdsfhsdfhsdfhsdfhdsfhsdfhsdfhdsfhsdfh')
    surfacing_sub_form = SurfacingForm(prefix='surfacing_sub_formhsdfhdfhsdfngnsd,gnsd.fgnsd')
    additional_surfacing_sub_form = AdditionalSurfacingForm(prefix='additional_surfacing_sub_ffhsdfhsdfhsdflkgldksfkgdorm')
    final_surfacing_sub_form = FinalSurfacingForm(prefix='final_surfacing_sub_fgsndfgnskldjfklgjkldsfjgj;dsfkgorm')
    heat_treatment_sub_form = HeatTreatmentForm(prefix='heat_treatment_sdklfh;skldfkhlj;sdfjhkl;sdsub_form')
    machining_sub_form = MachiningForm(prefix='machining_sub_fofsgdfjgklsdjfhkjds;hdfkhjd;rm')

    ######################################### Проверяем метод
    if request.POST:
        ### Загружаем наши формы снова, указываем в аргументе какой метод используем
        form = PrimaryTableForm(request.POST, prefix="primary_table_flgd;lsfjg;sdfjgj;sldkjfkjgsdf;gjs;dlfjgsdorm")
        gouging_sub_form = GougingForm(request.POST, prefix='gouging_suflgsd;fkgjsdfjg;kjsdfgsdb_form')
        surfacing_sub_form = SurfacingForm(request.POST, prefix='surfacing_sub_fadg,a;sdjhgahsdk;lgjaksdgorm')
        additional_surfacing_sub_form = AdditionalSurfacingForm(request.POST, prefix='additional_surfacing_sub_form')
        final_surfacing_sub_form = FinalSurfacingForm(request.POST, prefix='final_surfacing_sub_gdfjgjsdfjhgfsdgform')
        heat_treatment_sub_form = HeatTreatmentForm(request.POST, prefix='heat_treatment_sub_fdgsdfkhjsd;fjhorm')
        machining_sub_form = MachiningForm(request.POST, prefix='machining_sub_fobdnmfgbsmdnfgbnmdfmgkdfgkjfkgrm')

        # Убеждаемся в валидности всех форм
        if form.is_valid() \
                and gouging_sub_form.is_valid() and heat_treatment_sub_form.is_valid()                 and machining_sub_form.is_valid()  and surfacing_sub_form.is_valid() and additional_surfacing_sub_form.is_valid()             and final_surfacing_sub_form.is_valid():

            #### Подготавливаем модель главной таблицы, но не коммитим её в бд.
            pt = form.save(commit=False)

            # Сохраняем все поля с ForeignKey (наши подформы)
            pt.gouging = gouging_sub_form.save()

            #### Для наплавки, т.к. там есть своя подформа (дополнительная наплавка)
            #### делаем так:
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
            return redirect('/ ' )
        else:
            print(form.errors, gouging_sub_form.errors, surfacing_sub_form.errors,heat_treatment_sub_form.errors, machining_sub_form.errors,
                  additional_surfacing_sub_form.errors, final_surfacing_sub_form.errors)
