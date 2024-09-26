from django import forms
from .models import TrainingProgram

# Form for creating and editing training programs
class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgram
        fields = ['program_name', 'program_code', 'description']

class ExcelImportForm(forms.Form):
    excel_file = forms.FileField(label="upload excel file" , required=True)
