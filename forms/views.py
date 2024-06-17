from django.shortcuts import render
from forms_builder.models import Form
from forms_builder.views import get_form_with_fields_and_choices
from forms.models import Submission

def forms_list(request):
    forms = Form.objects.filter(status='published')    
    return render(request, 'forms/list.html', {'forms': forms})

def submit_form(request, pk):
    form = get_form_with_fields_and_choices(pk)
    if request.method == "POST":
        form_dt = Form.objects.get(pk=pk)
        submission = Submission.objects.create(
            form=form_dt, user = request.user, data = request.POST
        )
    return render(request, 'forms/submit.html', {'form': form})

def submissions_list(request, pk):
    form = Form.objects.get(pk=pk)
    submissions = Submission.objects.filter(form=form)
    return render(request, 'forms/submissions.html', {'submissions': submissions}) 