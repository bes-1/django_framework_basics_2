from django.urls import path
from basketapp.views import basket, basket_add, basket_remove, basket_edit

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='basket'),
    path('add/<int:pk>/', basket_add, name='basket_add'),
    path('remove/<int:pk>/', basket_remove, name='basket_remove'),
    path('edit/<int:pk>/<quantity>/', basket_edit, name='basket_edit'),
]
