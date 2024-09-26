from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'subject']



class ExcelImportForm(forms.Form):
    excel_file = forms.FileField(label='enter your excel file')