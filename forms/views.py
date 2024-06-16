from django.shortcuts import render
from forms_builder.models import Form


def submit_form(request, pk):
    form = Form.objects.get(pk=pk)
    return render(request, 'forms/submit.html', {'form': form})

def forms_list(request):
    forms = Form.objects.filter(status='published')
    print(forms)
    return render(request, 'forms/list.html', {'forms': forms})