from django.urls import path
from adminapp.views import users, user_update, user_delete, categories, category_create, category_update, \
    category_delete, product_create, products, product_delete, product_update, product_read, user_create

app_name = 'adminapp'

urlpatterns = [
    path('users/', users, name='users'),
    path('users/user_create/', user_create, name='user_create'),
    path('users/user_update/<int:pk>/', user_update, name='user_update'),
    path('users/user_delete/<int:pk>/', user_delete, name='user_delete'),

    path('categories/', categories, name='categories'),
    path('categories/category_create/', category_create, name='category_create'),
    path('categories/category_update/<int:pk>/', category_update, name='category_update'),
    path('categories/category_delete/<int:pk>/', category_delete, name='category_delete'),

    path('products/<int:pk>/', products, name='products'),
    path('products/product_create/', product_create, name='product_create'),
    path('products/product_update/<int:pk>/', product_update, name='product_update'),
    path('products/product_delete/<int:pk>/', product_delete, name='product_delete'),
    path('products/read/<int:pk>/', product_read, name='product_read'),

]
