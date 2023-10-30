from django import forms
from catalog.models import Product

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'purchase_price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Данный продукт запрещен к добавлению')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Описание содержит запрещенные слова')
        return cleaned_data


# class VersionForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#     class Meta:
#         model = Version
#         fields = ('product', 'version_number', 'version_name', 'is_active')
