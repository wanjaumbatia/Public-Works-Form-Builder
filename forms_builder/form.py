from django import forms
from forms_builder.models import Form


class FormBuilderForm(forms.ModelForm):
    
    class Meta:
        model = Form
        fields = ("name", "description")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
        }
