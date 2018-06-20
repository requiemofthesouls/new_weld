from django.urls import path
from IS import views
app_name = 'IS'

urlpatterns = [
    path('main/', views.main, name='main')
]