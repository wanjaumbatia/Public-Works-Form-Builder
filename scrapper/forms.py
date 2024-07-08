from django import forms

class LocationInputForm(forms.Form):
    locations = forms.CharField(widget=forms.Textarea, help_text="Enter multiple locations separated by commas")
