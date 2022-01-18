from django.urls import path
from adminapp.views import user_update, user_delete, categories, products, product_delete, \
    product_update, user_create, UsersListView, \
    ProductCategoryCreateView, ProductCategoryUpdateView, ProductCategoryDeleteView, ProductDetailView, \
    ProductCreateView

app_name = 'adminapp'

urlpatterns = [
    path('users/', UsersListView.as_view(), name='users'),
    path('users/user_create/', user_create, name='user_create'),
    path('users/user_update/<int:pk>/', user_update, name='user_update'),
    path('users/user_delete/<int:pk>/', user_delete, name='user_delete'),

    path('categories/', categories, name='categories'),
    path('categories/category_create/', ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/category_update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/category_delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/<int:pk>/', products, name='products'),
    path('products/product_create/<int:pk>/', ProductCreateView.as_view(), name='product_create'),
    path('products/product_update/<int:pk>/', product_update, name='product_update'),
    path('products/product_delete/<int:pk>/', product_delete, name='product_delete'),
    path('products/read/<int:pk>/', ProductDetailView.as_view(), name='product_read'),

]
