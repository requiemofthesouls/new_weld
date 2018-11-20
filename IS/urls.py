from django.urls import path
from IS import views

app_name = 'IS'

urlpatterns = [
    path('main/', views.Main.as_view(), name='main'),
    # path('main/add', views.dynamic_fields_in_surfacing, name='add__'),
    path('main/<int:pk>/', views.Main.as_view(), name='main-update'),
    path('main/search/', views.search, name='search'),

    # Формы
    # path('main/add_gouging/', views.add_gouging, name='add_gouging'),
    # path('main/add_surfacing', views.add_surfacing, name='add_surfacing'),
    # path('main/add_heat_treatment', views.add_heat_treatment, name='add_heat_treatment'),
    # path('main/add_machining', views.add_machining, name='add_machining'),
    path(
        'main/add_primary_table',
        views.add_primary_table,
        name='add_primary_table')

]
