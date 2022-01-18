from django.contrib.auth.forms import UserChangeForm

# from authapp.forms import ShopUserEditForm
from django.forms import HiddenInput, forms
from django import forms

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class ShopUserAdminEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'password':
                field.widget = HiddenInput()

    def clean_age(self):
        data_age = self.cleaned_data['age']
        if data_age < 18:
            raise forms.ValidationError("Вам меньше 18 лет!")

        return data_age


# class ShopUserAdminEditForm(ShopUserEditForm):
#     class Meta:
#         model: ShopUser
#         fields = '__all__'


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'