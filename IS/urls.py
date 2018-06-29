from django.urls import path
from IS import views
app_name = 'IS'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('main/search/', views.search, name='search'),

    # Формы
    path('main/add_gouging/', views.add_gouging, name='add_gouging')
]